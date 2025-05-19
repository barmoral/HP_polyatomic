"""
openMM code to calculate osmotic pressure and osmotic coefficients from harmonic potentials

"""

# Imports
import logging
logging.basicConfig(
    level=logging.INFO
)

import warnings
warnings.filterwarnings('ignore')

from typing import Union, Iterable, Optional

import argparse
from argparse import Namespace

import os
import os.path
import shutil
import pickle
from pathlib import Path
import numpy as np
import pandas as pd
import math
import json
import csv
from dataclasses import dataclass
from tqdm import tqdm
import subprocess
import shutil
from builtins import sum
from tqdm.notebook import tqdm 

from openmm import CustomExternalForce, System, CustomCentroidBondForce, CustomNonbondedForce
from openmm.app import Topology as OMMTopology

from openff.toolkit import Molecule, Topology
from openff.toolkit import ForceField as ForceField
from openff.interchange import Interchange

from polymerist.genutils.fileutils.pathutils import assemble_path
from polymerist.genutils.decorators.functional import allow_string_paths

from polymerist.mdtools.openfftools import topology
from polymerist.mdtools.openfftools import boxvectors
from polymerist.mdtools.openfftools import TKWRAPPERS, GTR

from polymerist.mdtools.openfftools.unitsys import openff_to_openmm
from polymerist.mdtools.openfftools.solvation.solvents import water_TIP3P
from polymerist.mdtools.openfftools.partialcharge.molchargers import NAGLCharger
from polymerist.mdtools.openfftools import FF_PATH_REGISTRY, FF_DIR_REGISTRY

from polymerist.mdtools.openmmtools.execution import run_simulation_schedule
from polymerist.mdtools.openmmtools.parameters import SimulationParameters

from openff.units import UnitRegistry
ureg = UnitRegistry()

from polymerist.mdtools.openfftools.partialcharge.molchargers import NAGLCharger, EspalomaCharger, ABE10Charger
from openff.toolkit.utils.nagl_wrapper import NAGLToolkitWrapper
from openff.toolkit.utils.openeye_wrapper import OpenEyeToolkitWrapper
from openff.toolkit.utils.rdkit_wrapper import RDKitToolkitWrapper
from openff.toolkit.utils.ambertools_wrapper import AmberToolsToolkitWrapper
from openff.toolkit.utils.builtin_wrapper import BuiltInToolkitWrapper

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

from scipy.optimize import least_squares, minimize
from scipy.integrate import simpson
from scipy.integrate import quad, simpson, trapezoid
from timeit import default_timer as timer

# from openmm.unit import *
from openmm.unit import bar, mole, litre, kelvin, kilojoule_per_mole, nanometer, angstrom, kilocalorie_per_mole, kilogram, molar, atmosphere, nanosecond, picosecond, femtoseconds
from openmm.unit import Quantity, Unit
from openmm.unit import AVOGADRO_CONSTANT_NA, BOLTZMANN_CONSTANT_kB

import MDAnalysis as mda
from MDAnalysis.lib.distances import distance_array
from MDAnalysis import units
from MDAnalysis.analysis import rdf
from MDAnalysis.analysis import density
from pymbar import timeseries

from salt_data import SaltData, salt_infos

## Loading information for specified salt
def load_salt_info(ion1, ion2):
    """
    Load all data entries for a specific salt from salt_info and return them as a dictionary
    where the salt appears only once with a subdictionary containing all its data.
    """
    salt = ion1 + ion2
    print(f"Salt to be analyzed: {salt}")

    # Convert dictionaries into SaltData instances
    salt_info_cleaned = [SaltData(**entry) if isinstance(entry, dict) else entry for entry in salt_infos]

    # Filter all entries that match the requested salt and store in a subdictionary
    filtered_entries = {
        f"Molality {entry.molality} mol/kg": {
            "Molarity": entry.molarity,
            "Number of Particles": math.ceil(entry.num_particles),
            "Osmotic Coefficient": entry.osmotic_coefficient,
        }
        for entry in salt_info_cleaned if entry.salt == salt
    }

    # Return results with the salt name as the top-level key
    if filtered_entries:
        return {salt: filtered_entries}
    else:
        return {"Error": f"No data found for {salt}"}

# Applying restraints - Harmonic Potential
def insert_harmonic_potential_OpenMM(
        openmm_system : System,
        openmm_topology : OMMTopology,
        k : Quantity=0.68095403*(kilojoule_per_mole/nanometer**2),
        delta_z : Optional[Quantity]= None,
        z_center : Quantity=7.2 * nanometer,
        target_residues : Optional[Iterable[str]]=None,
    ) -> None:
    '''Adds a custom harmonic force to an OpenMM System and registers selected particles to that force'''
    
    if target_residues is None:
        raise ValueError("target_residues must be specified")

    fb_force = CustomExternalForce('0.5*k*((z-z0)^2)')
    fb_force.addGlobalParameter('k', k)
    fb_force.addGlobalParameter('z0', z_center)
    openmm_system.addForce(fb_force)

    ## Applying custom external force to only the specified residues
    for atom in openmm_topology.atoms():
        res=atom.residue.name
        if res in target_residues:
            fb_force.addParticle(atom.index, [])

def insert_flat_bottom_potential_OpenMM(
        openmm_system : System,
        openmm_topology : OMMTopology,
        k : Quantity=4184*(kilojoule_per_mole/nanometer**2),
        z_center : Quantity=7.2 * nanometer,
        delta_z : Quantity= 2.4 * nanometer,
        target_residues : Optional[Iterable[str]]=None,
    ) -> None:
    '''Adds a custom flat-bottomed potential force to an OpenMM System and registers selected particles to that force'''
    if target_residues is None:
        raise ValueError("target_residues must be specified")
        
    fb_force = CustomExternalForce('0.5*k*(max(0, abs(z-z0)-rbf)^2)')
    fb_force.addGlobalParameter('k', k)
    fb_force.addGlobalParameter('rbf', delta_z)
    fb_force.addGlobalParameter('z0', z_center)
    openmm_system.addForce(fb_force)

    ## Applying custom external force to only the specified residues
    for atom in openmm_topology.atoms():
        res=atom.residue.name
        if res in target_residues:
            fb_force.addParticle(atom.index, [])

RESTRAINT_TYPES = {
    'FBP' : insert_flat_bottom_potential_OpenMM,
    'HP' : insert_harmonic_potential_OpenMM,
}
RESTRAINT_TYPE_ALIASES = {
    'FBP' : 'flat-bottomed potential',
    'HP' : 'harmonic potential',
}

def modify_omm_objects(ion1,ion2,center_atom1,center_atom2,concentration,repnum,wdir,input_picklefile):
    with open(input_picklefile, "rb") as f:
        omm_build = pickle.load(f)

    omm_objects_mod={}
    
    for r in tqdm(range(repnum), desc=f"Modifying {concentration}m systems", leave=False):
        rep_key = f'r{r}'
        print(rep_key)

        omm_top = omm_build[rep_key]["topology"]
        omm_pos = omm_build[rep_key]["positions"]
        omm_sys = omm_build[rep_key]["system"]

        # Step 1: Identify polyatomic center atoms for both ions
        poly_atoms = []

        for residue in omm_top.residues():
            if residue.name == ion1.upper():  
                for atom in residue.atoms():
                    if atom.element.symbol == f"{center_atom1}":  # Find the phosphorus atom
                        poly_atoms.append(atom.index)
            if residue.name == ion2.upper():  
                for atom in residue.atoms():
                    if atom.element.symbol == f"{center_atom2}":  # Find the phosphorus atom
                        poly_atoms.append(atom.index)

        # Step 2: Apply CustomExternalForce to dummy particles
        fb_force = CustomExternalForce('0.5*k*((z-z0)^2)')
        fb_force.addGlobalParameter('k', k)
        fb_force.addGlobalParameter('z0', z_center)

        for atom_index in poly_atoms:
            fb_force.addParticle(atom_index, [])

        omm_sys.addForce(fb_force)

        # Save each replicate's results in the dictionary
        omm_objects_mod[f"r{r}"] = {
            'topology': omm_top,
            'positions': omm_pos,
            'system': omm_sys
        }
        
    # Save the full dictionary
    output_picklefile = f"{wdir}/omm_modified_{concentration}.pkl"
    with open(output_picklefile, "wb") as f:
        pickle.dump(omm_objects_mod, f)
    print(f"✅ System dictionary for {concentration}m saved as pickle file")

    return omm_objects_mod

## Initializing paths and working directory
@allow_string_paths
def produce_interchange(pdb_path : Optional[str], working_dir : Path, file_prefix : str, ff_names : Optional[Iterable[str]]=None) -> Interchange:
    '''Load a valid OpenFF Interchange for the given PDB system, creating a new one and writing relevant files if none is found'''

    pdb_path = Path(pdb_path)
    if pdb_path.parent != working_dir:
        shutil.copy(pdb_path, working_dir)

    sdf_path = assemble_path(working_dir, file_prefix, extension='sdf') 
    inc_path = assemble_path(working_dir, file_prefix, extension='pkl') 

    ## Load topology from PDB
    if sdf_path.exists():
        offtop = topology.topology_from_sdf(sdf_path)
    else:
        assert(pdb_path.exists())
        offtop = Topology.from_pdb(pdb_path)
        # TODO : for non water/salts - will need to invoke NAGLCharger on !!UNIQUE!! molecules and cache those (as Molecule objects),
        # then pass to charge_from_molecules to avoid running repeated AM1-BCC
        # for salts, nedd to have the correct PDB residue codes to have them be correctly recognized by from_pdb() (i.e. NH4 for ammonium and PO4 for phosphate)

    ## Parameterize system with OpenFF  
    ### load interchange from file if already extant, otherwise make a new one and save it
    if inc_path.exists():
        with inc_path.open('rb') as file:
            inc  = pickle.load(file)
    else:
        if not ff_names:
            raise ValueError("Force field files must be specified.")
        ff = ForceField(ff_names) # load force fields
        inc = ff.create_interchange(topology=offtop, toolkit_registry=GTR) # convert to interchange for export
        inc.box = boxvectors.get_topology_bbox(offtop)

        if not sdf_path.exists():
            topology.topology_to_sdf(sdf_path, inc.topology)

        with inc_path.open('wb') as file:
            pickle.dump(inc, file)

    return inc


# read arguments from CLI to pass into OpenMM runner

def parse_args() -> Namespace:
    '''Read user inputs from the command line and preprocess basic parts of them'''
    parser = argparse.ArgumentParser(description='Run OpenMM simulation schedules according to presets of simulation parameters')

    parser.add_argument('-n', '--name', help='Tag to use to refer to working directory and internal files', required=True)
    parser.add_argument('-s', '--salt', help='Comma-separated list of ion residues to be used', nargs='+', required=True)
    parser.add_argument('-p', '--postfix', help='Optional extra modifier to "name"; will be appended to name with an underscore separator', default='')
    parser.add_argument('-c', '--cwd', help='The current working directory that all created files/directories should be made relative to', type=Path, default=Path.cwd())
    parser.add_argument('-pdb', '--pdb_path', help='A path to a PDB file containing the initial structure of the system being simulated', type=Path, required=True)
    parser.add_argument('-omm', '--openmm_dir', help='The directory path into which OpenMM setup, checkpoint, and output files should be written', type=Path)
    parser.add_argument('-spp', '--sim_param_paths',
        help='One or more serialized simulation presets; \
            \nsimulations built from these presets will be run in the order they are provided here',
        type=Path, nargs='+', required=True
    )
    parser.add_argument('-ff', '--ff_files', help='Force field file or files to be used', nargs='+', required=True)
    parser.add_argument('-r', '--restraint_type', help='The kind of potential restraint to apply to ions in the systems', choices=['HP', 'FBP'], required=True)
    parser.add_argument('-k', help='The spring constant to apply in the harmonic potential restraint') # this should also default to a float, but want to retain the NoneType value to check if this is unset
    parser.add_argument('--z_center', help='', type=float, default=7.2)
    parser.add_argument('--delta_z', help='', type=float, default=2.4)
    parser.add_argument('-du', '--distance_unit', help='The unit convention to use for units of length', choices=['angstrom', 'angstroms', 'nanometer', 'nanometers'], default='nanometer')

    args = parser.parse_args()

    salt_env = os.getenv('SALT')
    # Use environment variable if --salt isn't provided
    if not args.salt or args.salt == [""]:
        if salt_env:
            args.salt = salt_env.split()  # Convert "CS BR" -> ['CS', 'BR']
        else:
            raise ValueError("Salt must be provided via '--salt' argument or 'SALT' environment variable.")

    ff_env = os.getenv('FF_FILES')    
    # Use environment variable if --ff_files isn't provided 
    if not args.ff_files or args.ff_files == [""]:
        if ff_env:
            args.ff_files = ff_env.split()
        else:
            raise ValueError("Force field files must be provided via '--ff_files' argument or 'FF_FILES' environment variable.")

    # define directories
    if args.postfix != '':
        args.postfix = '_' + args.postfix
    args.file_prefix = f'{args.name}{args.postfix}'
    args.working_dir = args.cwd / args.file_prefix # Can change this to wherever your files are

    if args.openmm_dir is None:
        args.openmm_dir = args.working_dir / f'{args.file_prefix}_OpenMM'

    # define Quanitity parameters from restraint
    args.restraint_fn = RESTRAINT_TYPES[args.restraint_type]
    logging.info(f'Using restraint type {args.restraint_type} ({RESTRAINT_TYPE_ALIASES[args.restraint_type]})')

    args.distance_unit = getattr(openmm.unit, args.distance_unit) # convert string name of unit into OpenMM object

    args.delta_z = args.delta_z * args.distance_unit
    args.z_center = args.z_center * args.distance_unit

    # slightly more involved handling of force constants, as this default does differ between restraint implementations
    FORCE_CONST_UNIT = (kilojoule_per_mole/nanometer**2)
    if args.k is not None:
        args.k = float(args.k) * FORCE_CONST_UNIT # enforce Quantity with valid units
    else:
        if args.restraint_type == 'HP':
            args.k = 0.68095403 * FORCE_CONST_UNIT
        elif args.restraint_type == 'FBP':
            args.k = 4184 * FORCE_CONST_UNIT
        
    return args


def main():
    '''Run an OpenMM simulation schedule in a given working directory, with arbitrary PDB starting structure and output directory'''
    '''Ensure that a working directory is set up given a name handle that will be used to refer to it
    Returns the resulting path'''
    args = parse_args()
    ion1=args.salt[0]
    ion2=args.salt[1]
    salt_dict = load_salt_info(ion1,ion2)

    args.working_dir.mkdir(exist_ok=True)
    args.openmm_dir.mkdir(exist_ok=True)

    rdir=args.working_dir / 'result_files'
    inpickle=args.working_dir / f'omm_build'
    # Build simulation schedule based on serialized simulation parameter presets
    schedule = {
        path.stem : SimulationParameters.from_file(path)
            for path in args.sim_param_paths
    }

    # make Interchange and export to OpenMM objects
    inc = produce_interchange(args.pdb_path, working_dir=args.working_dir, file_prefix=args.file_prefix, ff_names=args.ff_files)

    ommtop = inc.to_openmm_topology()
    ommsys = inc.to_openmm_system(combine_nonbonded_forces=False, add_constrained_forces=True)
    ommpos = openff_to_openmm(inc.get_positions(include_virtual_sites=True))

    # apply appropriate restraint
    args.restraint_fn( 
        openmm_system=ommsys, 
        openmm_topology=ommtop, 
        k=args.k, 
        delta_z=args.delta_z, 
        z_center=args.z_center,
        target_residues=args.salt
    )

    history = run_simulation_schedule(
        working_dir=args.openmm_dir,
        schedule=schedule,
        init_top=ommtop,
        init_sys=ommsys,
        init_pos=ommpos,
        return_history=True
    )

if __name__ == '__main__':
    main()