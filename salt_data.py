from dataclasses import dataclass

@dataclass
class SaltData:
    salt: str
    molality: float
    molarity: float
    num_particles: float
    osmotic_coefficient: float
    density: str

salt_infos = [
    {
        "salt": "CsBr",
        "molality": 0.1,
        "molarity": 0.09924398867696552,
        "num_particles": 6.609501018088462,
        "osmotic_coefficient": 0.917,
        "density": 1.01356
    },
    {
        "salt": "CsBr",
        "molality": 0.2,
        "molarity": 0.19756331038345923,
        "num_particles": 13.157420600724755,
        "osmotic_coefficient": 0.896,
        "density": 1.02986
    },
    {
        "salt": "CsBr",
        "molality": 0.3,
        "molarity": 0.29496269656330865,
        "num_particles": 19.644073854981986,
        "osmotic_coefficient": 0.882,
        "density": 1.04598
    },
    {
        "salt": "CsBr",
        "molality": 0.4,
        "molarity": 0.3914465074959176,
        "num_particles": 26.06975116893849,
        "osmotic_coefficient": 0.873,
        "density": 1.06192
    },
    {
        "salt": "CsBr",
        "molality": 0.5,
        "molarity": 0.48702328713265036,
        "num_particles": 32.43502155695971,
        "osmotic_coefficient": 0.865,
        "density": 1.07769
    },
    {
        "salt": "CsBr",
        "molality": 0.6,
        "molarity": 0.5816991609366436,
        "num_particles": 38.74029296571705,
        "osmotic_coefficient": 0.861,
        "density": 1.09329
    },
    {
        "salt": "CsBr",
        "molality": 0.7,
        "molarity": 0.6754858929803901,
        "num_particles": 44.986348864820656,
        "osmotic_coefficient": 0.857,
        "density": 1.10873
    },
    {
        "salt": "CsBr",
        "molality": 0.8,
        "molarity": 0.7683909735372332,
        "num_particles": 51.173688095257766,
        "osmotic_coefficient": 0.854,
        "density": 1.12401
    },
    {
        "salt": "CsBr",
        "molality": 0.9,
        "molarity": 0.8604138044478984,
        "num_particles": 57.302270820516505,
        "osmotic_coefficient": 0.852,
        "density": 1.13912
    },
    {
        "salt": "CsBr",
        "molality": 1.0,
        "molarity": 0.951583512668926,
        "num_particles": 63.37403685228191,
        "osmotic_coefficient": 0.85,
        "density": 1.15409
    },
    {
        "salt": "CsBr",
        "molality": 1.2,
        "molarity": 1.131374604499702,
        "num_particles": 75.34785431307247,
        "osmotic_coefficient": 0.849,
        "density": 1.18358
    },
    {
        "salt": "CsBr",
        "molality": 1.4,
        "molarity": 1.3077721979700045,
        "num_particles": 87.09566986515863,
        "osmotic_coefficient": 0.848,
        "density": 1.21243
    },
    {
        "salt": "CsBr",
        "molality": 1.6,
        "molarity": 1.4809204951003214,
        "num_particles": 98.62708714714796,
        "osmotic_coefficient": 0.848,
        "density": 1.24073
    },
    {
        "salt": "CsBr",
        "molality": 1.8,
        "molarity": 1.6508678594823933,
        "num_particles": 109.94532710182105,
        "osmotic_coefficient": 0.85,
        "density": 1.26847
    },
    {
        "salt": "CsBr",
        "molality": 2.0,
        "molarity": 1.8176793254864554,
        "num_particles": 121.0547209208401,
        "osmotic_coefficient": 0.852,
        "density": 1.29566
    },
    {
        "salt": "CsBr",
        "molality": 2.5,
        "molarity": 2.2215042182732,
        "num_particles": 147.94885401227788,
        "osmotic_coefficient": 0.859,
        "density": 1.36136
    },
    {
        "salt": "CsBr",
        "molality": 3.0,
        "molarity": 2.607300891707305,
        "num_particles": 173.64233469389112,
        "osmotic_coefficient": 0.866,
        "density": 1.42396
    },
    {
        "salt": "CsBr",
        "molality": 3.5,
        "molarity": 2.976123816865205,
        "num_particles": 198.20538916019456,
        "osmotic_coefficient": 0.874,
        "density": 1.48367
    },
    {
        "salt": "CsBr",
        "molality": 4.0,
        "molarity": 3.328947084116592,
        "num_particles": 221.70289037101188,
        "osmotic_coefficient": 0.884,
        "density": 1.54067
    },
    {
        "salt": "CsBr",
        "molality": 4.5,
        "molarity": 3.666716897088083,
        "num_particles": 244.1978540708413,
        "osmotic_coefficient": 0.892,
        "density": 1.59514
    },
    {
        "salt": "CsBr",
        "molality": 5.0,
        "molarity": 3.9903103122501875,
        "num_particles": 265.74869090713895,
        "osmotic_coefficient": 0.901,
        "density": 1.64724
    },
    {
        "salt": "CsCl",
        "molality": 0.1,
        "molarity": 0.09931100000393378,
        "num_particles": 6.613963872108385,
        "osmotic_coefficient": 0.917,
        "density": 1.00983
    },
    {
        "salt": "CsCl",
        "molality": 0.2,
        "molarity": 0.19783064647199497,
        "num_particles": 13.175224783858711,
        "osmotic_coefficient": 0.897,
        "density": 1.02246
    },
    {
        "salt": "CsCl",
        "molality": 0.3,
        "molarity": 0.29555986246654004,
        "num_particles": 19.68384420982154,
        "osmotic_coefficient": 0.885,
        "density": 1.03496
    },
    {
        "salt": "CsCl",
        "molality": 0.4,
        "molarity": 0.39249576518910495,
        "num_particles": 26.13963015993645,
        "osmotic_coefficient": 0.875,
        "density": 1.04732
    },
    {
        "salt": "CsCl",
        "molality": 0.5,
        "molarity": 0.48864579682340575,
        "num_particles": 32.54307827249351,
        "osmotic_coefficient": 0.869,
        "density": 1.05956
    },
    {
        "salt": "CsCl",
        "molality": 0.6,
        "molarity": 0.5840133113415245,
        "num_particles": 38.89441191701047,
        "osmotic_coefficient": 0.864,
        "density": 1.07168
    },
    {
        "salt": "CsCl",
        "molality": 0.7,
        "molarity": 0.6786014606584772,
        "num_particles": 45.19384100630711,
        "osmotic_coefficient": 0.861,
        "density": 1.08368
    },
    {
        "salt": "CsCl",
        "molality": 0.8,
        "molarity": 0.772420260018613,
        "num_particles": 51.442032540658225,
        "osmotic_coefficient": 0.859,
        "density": 1.09557
    },
    {
        "salt": "CsCl",
        "molality": 0.9,
        "molarity": 0.8654669811484605,
        "num_particles": 57.63880482113652,
        "osmotic_coefficient": 0.858,
        "density": 1.10734
    },
    {
        "salt": "CsCl",
        "molality": 1.0,
        "molarity": 0.957752747440857,
        "num_particles": 63.784898649046525,
        "osmotic_coefficient": 0.857,
        "density": 1.119
    },
    {
        "salt": "CsCl",
        "molality": 1.2,
        "molarity": 1.1400794654385242,
        "num_particles": 75.92758501519829,
        "osmotic_coefficient": 0.856,
        "density": 1.14201
    },
    {
        "salt": "CsCl",
        "molality": 1.4,
        "molarity": 1.3193968782167895,
        "num_particles": 87.86985616047338,
        "osmotic_coefficient": 0.856,
        "density": 1.16456
    },
    {
        "salt": "CsCl",
        "molality": 1.6,
        "molarity": 1.4958026620953917,
        "num_particles": 99.61821718148634,
        "osmotic_coefficient": 0.857,
        "density": 1.18671
    },
    {
        "salt": "CsCl",
        "molality": 1.8,
        "molarity": 1.6693245375458157,
        "num_particles": 111.17451422012391,
        "osmotic_coefficient": 0.859,
        "density": 1.20845
    },
    {
        "salt": "CsCl",
        "molality": 2.0,
        "molarity": 1.8400113711173616,
        "num_particles": 122.54200171538692,
        "osmotic_coefficient": 0.864,
        "density": 1.22979
    },
    {
        "salt": "CsCl",
        "molality": 2.5,
        "molarity": 2.254715321275248,
        "num_particles": 150.1606637352664,
        "osmotic_coefficient": 0.871,
        "density": 1.28149
    },
    {
        "salt": "CsCl",
        "molality": 3.0,
        "molarity": 2.652875594652776,
        "num_particles": 176.67754165738435,
        "osmotic_coefficient": 0.88,
        "density": 1.33093
    },
    {
        "salt": "CsCl",
        "molality": 3.5,
        "molarity": 3.035252255766835,
        "num_particles": 202.143254640293,
        "osmotic_coefficient": 0.891,
        "density": 1.37823
    },
    {
        "salt": "CsCl",
        "molality": 4.0,
        "molarity": 3.402619753322497,
        "num_particles": 226.60937980793577,
        "osmotic_coefficient": 0.901,
        "density": 1.42352
    },
    {
        "salt": "CsCl",
        "molality": 4.5,
        "molarity": 3.7557776993889465,
        "num_particles": 250.12917012662126,
        "osmotic_coefficient": 0.913,
        "density": 1.46694
    },
    {
        "salt": "CsCl",
        "molality": 5.0,
        "molarity": 4.095395808448257,
        "num_particles": 272.74722757789124,
        "osmotic_coefficient": 0.923,
        "density": 1.50858
    },
    {
        "salt": "CsCl",
        "molality": 5.5,
        "molarity": 4.422177281176337,
        "num_particles": 294.5103842736478,
        "osmotic_coefficient": 0.934,
        "density": 1.54855
    },
    {
        "salt": "CsCl",
        "molality": 6.0,
        "molarity": 4.736846818163728,
        "num_particles": 315.46690418790945,
        "osmotic_coefficient": 0.945,
        "density": 1.58697
    },
    {
        "salt": "CsI",
        "molality": 0.1,
        "molarity": 0.09913049072058841,
        "num_particles": 6.601942224168286,
        "osmotic_coefficient": 0.916,
        "density": 1.01706
    },
    {
        "salt": "CsI",
        "molality": 0.2,
        "molarity": 0.19711738636946963,
        "num_particles": 13.127722729208852,
        "osmotic_coefficient": 0.895,
        "density": 1.0368
    },
    {
        "salt": "CsI",
        "molality": 0.3,
        "molarity": 0.29396823394186894,
        "num_particles": 19.577844133701326,
        "osmotic_coefficient": 0.88,
        "density": 1.05627
    },
    {
        "salt": "CsI",
        "molality": 0.4,
        "molarity": 0.3897007402683518,
        "num_particles": 25.95348568604361,
        "osmotic_coefficient": 0.87,
        "density": 1.0755
    },
    {
        "salt": "CsI",
        "molality": 0.5,
        "molarity": 0.4843283284877932,
        "num_particles": 32.25554134718229,
        "osmotic_coefficient": 0.863,
        "density": 1.09449
    },
    {
        "salt": "CsI",
        "molality": 0.6,
        "molarity": 0.5778684057078294,
        "num_particles": 38.48517040441706,
        "osmotic_coefficient": 0.858,
        "density": 1.11325
    },
    {
        "salt": "CsI",
        "molality": 0.7,
        "molarity": 0.6703283872043131,
        "num_particles": 44.64286670401458,
        "osmotic_coefficient": 0.855,
        "density": 1.13177
    },
    {
        "salt": "CsI",
        "molality": 0.8,
        "molarity": 0.7617382319629623,
        "num_particles": 50.73062546955711,
        "osmotic_coefficient": 0.852,
        "density": 1.15008
    },
    {
        "salt": "CsI",
        "molality": 0.9,
        "molarity": 0.8520986295507726,
        "num_particles": 56.74849262517386,
        "osmotic_coefficient": 0.849,
        "density": 1.16816
    },
    {
        "salt": "CsI",
        "molality": 1.0,
        "molarity": 0.9414276756018766,
        "num_particles": 62.697673312998006,
        "osmotic_coefficient": 0.846,
        "density": 1.18602
    },
    {
        "salt": "CsI",
        "molality": 1.2,
        "molarity": 1.1170904699902118,
        "num_particles": 74.39655234666026,
        "osmotic_coefficient": 0.842,
        "density": 1.22114
    },
    {
        "salt": "CsI",
        "molality": 1.4,
        "molarity": 1.2887747903916746,
        "num_particles": 85.83047097095947,
        "osmotic_coefficient": 0.839,
        "density": 1.25539
    },
    {
        "salt": "CsI",
        "molality": 1.6,
        "molarity": 1.4566517105367256,
        "num_particles": 97.01082244014425,
        "osmotic_coefficient": 0.836,
        "density": 1.28886
    },
    {
        "salt": "CsI",
        "molality": 1.8,
        "molarity": 1.6208067547071596,
        "num_particles": 107.943302543301,
        "osmotic_coefficient": 0.834,
        "density": 1.32155
    },
    {
        "salt": "CsI",
        "molality": 2.0,
        "molarity": 1.7813532330451036,
        "num_particles": 118.6354575662021,
        "osmotic_coefficient": 0.832,
        "density": 1.35349
    },
    {
        "salt": "CsI",
        "molality": 2.5,
        "molarity": 2.167533077704188,
        "num_particles": 144.35445687756177,
        "osmotic_coefficient": 0.827,
        "density": 1.43016
    },
    {
        "salt": "CsI",
        "molality": 3.0,
        "molarity": 2.5331313960088346,
        "num_particles": 168.70275735660977,
        "osmotic_coefficient": 0.822,
        "density": 1.50251
    },
    {
        "salt": "CsNO3",
        "molality": 0.1,
        "molarity": 0.0991975310034585,
        "num_particles": 6.606407006607907,
        "osmotic_coefficient": 0.902,
        "density": 1.01131
    },
    {
        "salt": "CsNO3",
        "molality": 0.2,
        "molarity": 0.19737777990806776,
        "num_particles": 13.145064548914124,
        "osmotic_coefficient": 0.869,
        "density": 1.02536
    },
    {
        "salt": "CsNO3",
        "molality": 0.3,
        "molarity": 0.29454309334019096,
        "num_particles": 19.616128908720135,
        "osmotic_coefficient": 0.842,
        "density": 1.03922
    },
    {
        "salt": "CsNO3",
        "molality": 0.4,
        "molarity": 0.39069935890276153,
        "num_particles": 26.019992191564032,
        "osmotic_coefficient": 0.82,
        "density": 1.0529
    },
    {
        "salt": "CsNO3",
        "molality": 0.5,
        "molarity": 0.48586024672526584,
        "num_particles": 32.357564807597214,
        "osmotic_coefficient": 0.802,
        "density": 1.06642
    },
    {
        "salt": "CsNO3",
        "molality": 0.6,
        "molarity": 0.580034891551664,
        "num_particles": 38.62945511708725,
        "osmotic_coefficient": 0.787,
        "density": 1.07978
    },
    {
        "salt": "CsNO3",
        "molality": 0.7,
        "molarity": 0.6732318014441091,
        "num_particles": 44.83622974423183,
        "osmotic_coefficient": 0.774,
        "density": 1.09298
    },
    {
        "salt": "CsNO3",
        "molality": 0.8,
        "molarity": 0.7654727523010066,
        "num_particles": 50.97933893125321,
        "osmotic_coefficient": 0.761,
        "density": 1.10604
    },
    {
        "salt": "CsNO3",
        "molality": 0.9,
        "molarity": 0.8567619112114742,
        "num_particles": 57.05906020004596,
        "osmotic_coefficient": 0.748,
        "density": 1.11895
    },
    {
        "salt": "CsNO3",
        "molality": 1.0,
        "molarity": 0.9471249323171348,
        "num_particles": 63.077102078022556,
        "osmotic_coefficient": 0.736,
        "density": 1.13173
    },
    {
        "salt": "CsNO3",
        "molality": 1.2,
        "molarity": 1.1251314133184298,
        "num_particles": 74.93206713020285,
        "osmotic_coefficient": 0.715,
        "density": 1.15691
    },
    {
        "salt": "CsNO3",
        "molality": 1.4,
        "molarity": 1.2995757479483068,
        "num_particles": 86.54979856871711,
        "osmotic_coefficient": 0.695,
        "density": 1.18157
    },
    {
        "salt": "KBr",
        "molality": 0.1,
        "molarity": 0.09936553031613196,
        "num_particles": 6.617595509236188,
        "osmotic_coefficient": 0.928,
        "density": 1.00548
    },
    {
        "salt": "KBr",
        "molality": 0.2,
        "molarity": 0.1980464160787591,
        "num_particles": 13.18959471653264,
        "osmotic_coefficient": 0.916,
        "density": 1.0138
    },
    {
        "salt": "KBr",
        "molality": 0.3,
        "molarity": 0.29604018767585927,
        "num_particles": 19.715833149427166,
        "osmotic_coefficient": 0.91,
        "density": 1.02203
    },
    {
        "salt": "KBr",
        "molality": 0.4,
        "molarity": 0.3933483059577657,
        "num_particles": 26.1964080983642,
        "osmotic_coefficient": 0.906,
        "density": 1.03018
    },
    {
        "salt": "KBr",
        "molality": 0.5,
        "molarity": 0.4899759415045385,
        "num_particles": 32.63166391623227,
        "osmotic_coefficient": 0.904,
        "density": 1.03826
    },
    {
        "salt": "KBr",
        "molality": 0.6,
        "molarity": 0.5859149681743868,
        "num_particles": 39.02105941415783,
        "osmotic_coefficient": 0.904,
        "density": 1.04625
    },
    {
        "salt": "KBr",
        "molality": 0.7,
        "molarity": 0.6811825407038149,
        "num_particles": 45.36573707190112,
        "osmotic_coefficient": 0.904,
        "density": 1.05418
    },
    {
        "salt": "KBr",
        "molality": 0.8,
        "molarity": 0.7757695021628895,
        "num_particles": 51.66508705164202,
        "osmotic_coefficient": 0.905,
        "density": 1.06203
    },
    {
        "salt": "KBr",
        "molality": 0.9,
        "molarity": 0.8696842512585564,
        "num_particles": 57.91966869468518,
        "osmotic_coefficient": 0.906,
        "density": 1.06981
    },
    {
        "salt": "KBr",
        "molality": 1.0,
        "molarity": 0.9629294675076541,
        "num_particles": 64.12966045283923,
        "osmotic_coefficient": 0.907,
        "density": 1.07752
    },
    {
        "salt": "KBr",
        "molality": 1.2,
        "molarity": 1.1474424624939534,
        "num_particles": 76.41794959226549,
        "osmotic_coefficient": 0.91,
        "density": 1.09275
    },
    {
        "salt": "KBr",
        "molality": 1.4,
        "molarity": 1.3292767684082363,
        "num_particles": 88.52784205110018,
        "osmotic_coefficient": 0.914,
        "density": 1.10767
    },
    {
        "salt": "KBr",
        "molality": 1.6,
        "molarity": 1.5085443318700757,
        "num_particles": 100.46679330655566,
        "osmotic_coefficient": 0.917,
        "density": 1.12236
    },
    {
        "salt": "KBr",
        "molality": 1.8,
        "molarity": 1.6852527862707707,
        "num_particles": 112.23531173106063,
        "osmotic_coefficient": 0.922,
        "density": 1.1368
    },
    {
        "salt": "KBr",
        "molality": 2.0,
        "molarity": 1.8594124090067556,
        "num_particles": 123.83408178382622,
        "osmotic_coefficient": 0.927,
        "density": 1.15098
    },
    {
        "salt": "KBr",
        "molality": 2.5,
        "molarity": 2.284018173340373,
        "num_particles": 152.11218979885248,
        "osmotic_coefficient": 0.941,
        "density": 1.18541
    },
    {
        "salt": "KBr",
        "molality": 3.0,
        "molarity": 2.6935989966146066,
        "num_particles": 179.3896592406755,
        "osmotic_coefficient": 0.955,
        "density": 1.21841
    },
    {
        "salt": "KBr",
        "molality": 3.5,
        "molarity": 3.0887810649717933,
        "num_particles": 205.70819316859857,
        "osmotic_coefficient": 0.969,
        "density": 1.25008
    },
    {
        "salt": "KBr",
        "molality": 4.0,
        "molarity": 3.4700895930103357,
        "num_particles": 231.10277008831392,
        "osmotic_coefficient": 0.984,
        "density": 1.28047
    },
    {
        "salt": "KBr",
        "molality": 4.5,
        "molarity": 3.8381800432299644,
        "num_particles": 255.6170428206829,
        "osmotic_coefficient": 1.0,
        "density": 1.30968
    },
    {
        "salt": "KBr",
        "molality": 5.0,
        "molarity": 4.193578723644366,
        "num_particles": 279.2860626912183,
        "osmotic_coefficient": 1.015,
        "density": 1.33776
    },
    {
        "salt": "KBr",
        "molality": 5.5,
        "molarity": 4.53686315775477,
        "num_particles": 302.14829190020265,
        "osmotic_coefficient": 1.028,
        "density": 1.36478
    },
    {
        "salt": "KCl",
        "molality": 0.1,
        "molarity": 0.09943271617466477,
        "num_particles": 6.622069986796932,
        "osmotic_coefficient": 0.927,
        "density": 1.00174
    },
    {
        "salt": "KCl",
        "molality": 0.2,
        "molarity": 0.19831507073344593,
        "num_particles": 13.20748671419757,
        "osmotic_coefficient": 0.913,
        "density": 1.00636
    },
    {
        "salt": "KCl",
        "molality": 0.3,
        "molarity": 0.2966385628527585,
        "num_particles": 19.755684040081995,
        "osmotic_coefficient": 0.906,
        "density": 1.01091
    },
    {
        "salt": "KCl",
        "molality": 0.4,
        "molarity": 0.3944027062113697,
        "num_particles": 26.266629576184403,
        "osmotic_coefficient": 0.902,
        "density": 1.01541
    },
    {
        "salt": "KCl",
        "molality": 0.5,
        "molarity": 0.49160992066091597,
        "num_particles": 32.740484480999825,
        "osmotic_coefficient": 0.899,
        "density": 1.01987
    },
    {
        "salt": "KCl",
        "molality": 0.6,
        "molarity": 0.5882491563998908,
        "num_particles": 39.176512854296114,
        "osmotic_coefficient": 0.898,
        "density": 1.02427
    },
    {
        "salt": "KCl",
        "molality": 0.7,
        "molarity": 0.6843286848423963,
        "num_particles": 45.57526555986518,
        "osmotic_coefficient": 0.897,
        "density": 1.02863
    },
    {
        "salt": "KCl",
        "molality": 0.8,
        "molarity": 0.7798414451746792,
        "num_particles": 51.936272358085354,
        "osmotic_coefficient": 0.897,
        "density": 1.03294
    },
    {
        "salt": "KCl",
        "molality": 0.9,
        "molarity": 0.8748021277220028,
        "num_particles": 58.26051160261893,
        "osmotic_coefficient": 0.897,
        "density": 1.03722
    },
    {
        "salt": "KCl",
        "molality": 1.0,
        "molarity": 0.9691952352577303,
        "num_particles": 64.54695120138052,
        "osmotic_coefficient": 0.897,
        "density": 1.04145
    },
    {
        "salt": "KCl",
        "molality": 1.2,
        "molarity": 1.1563253319373654,
        "num_particles": 77.00953539421144,
        "osmotic_coefficient": 0.899,
        "density": 1.04981
    },
    {
        "salt": "KCl",
        "molality": 1.4,
        "molarity": 1.341176923547361,
        "num_particles": 89.32037456169355,
        "osmotic_coefficient": 0.901,
        "density": 1.05797
    },
    {
        "salt": "KCl",
        "molality": 1.6,
        "molarity": 1.5238482152774213,
        "num_particles": 101.48600902238908,
        "osmotic_coefficient": 0.904,
        "density": 1.06601
    },
    {
        "salt": "KCl",
        "molality": 1.8,
        "molarity": 1.7043141024916466,
        "num_particles": 113.5047668451438,
        "osmotic_coefficient": 0.908,
        "density": 1.0739
    },
    {
        "salt": "KCl",
        "molality": 2.0,
        "molarity": 1.8826169221094795,
        "num_particles": 125.37946760538881,
        "osmotic_coefficient": 0.912,
        "density": 1.08166
    },
    {
        "salt": "KCl",
        "molality": 2.5,
        "molarity": 2.3189273741321537,
        "num_particles": 154.43709029156597,
        "osmotic_coefficient": 0.924,
        "density": 1.10045
    },
    {
        "salt": "KCl",
        "molality": 3.0,
        "molarity": 2.7420988892365727,
        "num_particles": 182.61967945585926,
        "osmotic_coefficient": 0.937,
        "density": 1.11846
    },
    {
        "salt": "KCl",
        "molality": 3.5,
        "molarity": 3.1524520937747873,
        "num_particles": 209.94858833314524,
        "osmotic_coefficient": 0.95,
        "density": 1.13572
    },
    {
        "salt": "KCl",
        "molality": 4.0,
        "molarity": 3.5504094422052854,
        "num_particles": 236.4519517576914,
        "osmotic_coefficient": 0.965,
        "density": 1.15229
    },
    {
        "salt": "KCl",
        "molality": 4.5,
        "molarity": 3.9364023827073225,
        "num_particles": 262.1585035320994,
        "osmotic_coefficient": 0.98,
        "density": 1.16822
    },
    {
        "salt": "KI",
        "molality": 0.1,
        "molarity": 0.09925238265722296,
        "num_particles": 6.610060044602783,
        "osmotic_coefficient": 0.932,
        "density": 1.009
    },
    {
        "salt": "KI",
        "molality": 0.2,
        "molarity": 0.19760151891516592,
        "num_particles": 13.159965231715326,
        "osmotic_coefficient": 0.922,
        "density": 1.02081
    },
    {
        "salt": "KI",
        "molality": 0.3,
        "molarity": 0.29505024972165195,
        "num_particles": 19.64990476420804,
        "osmotic_coefficient": 0.918,
        "density": 1.03248
    },
    {
        "salt": "KI",
        "molality": 0.4,
        "molarity": 0.391608740996071,
        "num_particles": 26.08055567708782,
        "osmotic_coefficient": 0.917,
        "density": 1.04403
    },
    {
        "salt": "KI",
        "molality": 0.5,
        "molarity": 0.48728007184478245,
        "num_particles": 32.45212303422692,
        "osmotic_coefficient": 0.917,
        "density": 1.05545
    },
    {
        "salt": "KI",
        "molality": 0.6,
        "molarity": 0.5820798673206828,
        "num_particles": 38.76564744074818,
        "osmotic_coefficient": 0.918,
        "density": 1.06676
    },
    {
        "salt": "KI",
        "molality": 0.7,
        "molarity": 0.6760111763286994,
        "num_particles": 45.02133194915372,
        "osmotic_coefficient": 0.919,
        "density": 1.07795
    },
    {
        "salt": "KI",
        "molality": 0.8,
        "molarity": 0.7690804001235026,
        "num_particles": 51.21960287341806,
        "osmotic_coefficient": 0.922,
        "density": 1.08902
    },
    {
        "salt": "KI",
        "molality": 0.9,
        "molarity": 0.8613014003136167,
        "num_particles": 57.36138337590977,
        "osmotic_coefficient": 0.924,
        "density": 1.09998
    },
    {
        "salt": "KI",
        "molality": 1.0,
        "molarity": 0.9526735270275509,
        "num_particles": 63.44663017616083,
        "osmotic_coefficient": 0.926,
        "density": 1.11082
    },
    {
        "salt": "KI",
        "molality": 1.2,
        "molarity": 1.132952129153474,
        "num_particles": 75.45291509251277,
        "osmotic_coefficient": 0.931,
        "density": 1.1322
    },
    {
        "salt": "KI",
        "molality": 1.4,
        "molarity": 1.3099341650909384,
        "num_particles": 87.23965363765087,
        "osmotic_coefficient": 0.937,
        "density": 1.15312
    },
    {
        "salt": "KI",
        "molality": 1.6,
        "molarity": 1.4837242042632464,
        "num_particles": 98.81380997856392,
        "osmotic_coefficient": 0.943,
        "density": 1.17363
    },
    {
        "salt": "KI",
        "molality": 1.8,
        "molarity": 1.6543914858845947,
        "num_particles": 110.17999534322477,
        "osmotic_coefficient": 0.95,
        "density": 1.19374
    },
    {
        "salt": "KI",
        "molality": 2.0,
        "molarity": 1.8220043519336555,
        "num_particles": 121.34276120506402,
        "osmotic_coefficient": 0.957,
        "density": 1.21346
    },
    {
        "salt": "KI",
        "molality": 2.5,
        "molarity": 2.2280985182405457,
        "num_particles": 148.38802451447947,
        "osmotic_coefficient": 0.974,
        "density": 1.26111
    },
    {
        "salt": "KI",
        "molality": 3.0,
        "molarity": 2.6165741126685274,
        "num_particles": 174.25991732233283,
        "osmotic_coefficient": 0.99,
        "density": 1.30655
    },
    {
        "salt": "KI",
        "molality": 3.5,
        "molarity": 2.9884191736192904,
        "num_particles": 199.02424150649037,
        "osmotic_coefficient": 1.006,
        "density": 1.34992
    },
    {
        "salt": "KI",
        "molality": 4.0,
        "molarity": 3.3446649878318127,
        "num_particles": 222.74967921931298,
        "osmotic_coefficient": 1.021,
        "density": 1.39139
    },
    {
        "salt": "KI",
        "molality": 4.5,
        "molarity": 3.6862126810075666,
        "num_particles": 245.4962440829929,
        "osmotic_coefficient": 1.032,
        "density": 1.43108
    },
    {
        "salt": "KNO3",
        "molality": 0.1,
        "molarity": 0.09931885459798097,
        "num_particles": 6.614486976308888,
        "osmotic_coefficient": 0.906,
        "density": 1.00323
    },
    {
        "salt": "KNO3",
        "molality": 0.2,
        "molarity": 0.19786308185256868,
        "num_particles": 13.177384931629694,
        "osmotic_coefficient": 0.873,
        "density": 1.00932
    },
    {
        "salt": "KNO3",
        "molality": 0.3,
        "molarity": 0.29562928012956147,
        "num_particles": 19.688467322218877,
        "osmotic_coefficient": 0.851,
        "density": 1.01532
    },
    {
        "salt": "KNO3",
        "molality": 0.4,
        "molarity": 0.39261802453666583,
        "num_particles": 26.147772449388402,
        "osmotic_coefficient": 0.833,
        "density": 1.02124
    },
    {
        "salt": "KNO3",
        "molality": 0.5,
        "molarity": 0.48883367556624546,
        "num_particles": 32.555590715399426,
        "osmotic_coefficient": 0.817,
        "density": 1.02709
    },
    {
        "salt": "KNO3",
        "molality": 0.6,
        "molarity": 0.5842728849924205,
        "num_particles": 38.91169913342265,
        "osmotic_coefficient": 0.802,
        "density": 1.03286
    },
    {
        "salt": "KNO3",
        "molality": 0.7,
        "molarity": 0.6789483074383773,
        "num_particles": 45.21694048241071,
        "osmotic_coefficient": 0.79,
        "density": 1.03857
    },
    {
        "salt": "KNO3",
        "molality": 0.8,
        "molarity": 0.7728573213356316,
        "num_particles": 51.47114016982864,
        "osmotic_coefficient": 0.778,
        "density": 1.04421
    },
    {
        "salt": "KNO3",
        "molality": 0.9,
        "molarity": 0.866010234640578,
        "num_particles": 57.674984690135105,
        "osmotic_coefficient": 0.767,
        "density": 1.04979
    },
    {
        "salt": "KNO3",
        "molality": 1.0,
        "molarity": 0.9584024458379556,
        "num_particles": 63.828167589304975,
        "osmotic_coefficient": 0.756,
        "density": 1.0553
    },
    {
        "salt": "KNO3",
        "molality": 1.2,
        "molarity": 1.140965664299084,
        "num_particles": 75.98660453214015,
        "osmotic_coefficient": 0.736,
        "density": 1.06616
    },
    {
        "salt": "KNO3",
        "molality": 1.4,
        "molarity": 1.3205354906538553,
        "num_particles": 87.94568604359598,
        "osmotic_coefficient": 0.718,
        "density": 1.07675
    },
    {
        "salt": "KNO3",
        "molality": 1.6,
        "molarity": 1.4972251878245408,
        "num_particles": 99.71295526467314,
        "osmotic_coefficient": 0.7,
        "density": 1.08714
    },
    {
        "salt": "KNO3",
        "molality": 1.8,
        "molarity": 1.6710505886297649,
        "num_particles": 111.28946663738083,
        "osmotic_coefficient": 0.684,
        "density": 1.09731
    },
    {
        "salt": "KNO3",
        "molality": 2.0,
        "molarity": 1.8420796961320454,
        "num_particles": 122.67974906384133,
        "osmotic_coefficient": 0.669,
        "density": 1.10728
    },
    {
        "salt": "KNO3",
        "molality": 2.5,
        "molarity": 2.2577185697477087,
        "num_particles": 150.36067558586737,
        "osmotic_coefficient": 0.631,
        "density": 1.13135
    },
    {
        "salt": "KNO3",
        "molality": 3.0,
        "molarity": 2.6570509416948975,
        "num_particles": 176.95561351738993,
        "osmotic_coefficient": 0.602,
        "density": 1.15432
    },
    {
        "salt": "KNO3",
        "molality": 3.5,
        "molarity": 3.0409690446849345,
        "num_particles": 202.52398422077536,
        "osmotic_coefficient": 0.577,
        "density": 1.1763
    },
    {
        "salt": "LiBr",
        "molality": 0.1,
        "molarity": 0.09946321173766429,
        "num_particles": 6.624100945622545,
        "osmotic_coefficient": 0.943,
        "density": 1.00327
    },
    {
        "salt": "LiBr",
        "molality": 0.2,
        "molarity": 0.19843734181010036,
        "num_particles": 13.215629784789591,
        "osmotic_coefficient": 0.944,
        "density": 1.00942
    },
    {
        "salt": "LiBr",
        "molality": 0.3,
        "molarity": 0.2969201898341558,
        "num_particles": 19.774439975278483,
        "osmotic_coefficient": 0.952,
        "density": 1.01552
    },
    {
        "salt": "LiBr",
        "molality": 0.4,
        "molarity": 0.3949057635845982,
        "num_particles": 26.3001324438627,
        "osmotic_coefficient": 0.96,
        "density": 1.02156
    },
    {
        "salt": "LiBr",
        "molality": 0.5,
        "molarity": 0.4923988125615463,
        "num_particles": 32.7930235001373,
        "osmotic_coefficient": 0.97,
        "density": 1.02756
    },
    {
        "salt": "LiBr",
        "molality": 0.6,
        "molarity": 0.5894001275535663,
        "num_particles": 39.253165809436496,
        "osmotic_coefficient": 0.981,
        "density": 1.03352
    },
    {
        "salt": "LiBr",
        "molality": 0.7,
        "molarity": 0.6859104734530771,
        "num_particles": 45.6806103124499,
        "osmotic_coefficient": 0.993,
        "density": 1.03944
    },
    {
        "salt": "LiBr",
        "molality": 0.8,
        "molarity": 0.781930590307777,
        "num_particles": 52.07540629524591,
        "osmotic_coefficient": 1.007,
        "density": 1.04532
    },
    {
        "salt": "LiBr",
        "molality": 0.9,
        "molarity": 0.8774611943212538,
        "num_particles": 58.4376014559109,
        "osmotic_coefficient": 1.021,
        "density": 1.05116
    },
    {
        "salt": "LiBr",
        "molality": 1.0,
        "molarity": 0.9725121797496423,
        "num_particles": 64.7678547370858,
        "osmotic_coefficient": 1.035,
        "density": 1.05697
    },
    {
        "salt": "LiBr",
        "molality": 1.2,
        "molarity": 1.1611662232139786,
        "num_particles": 77.33193150351511,
        "osmotic_coefficient": 1.067,
        "density": 1.06848
    },
    {
        "salt": "LiBr",
        "molality": 1.4,
        "molarity": 1.3478699302682011,
        "num_particles": 89.76611878585464,
        "osmotic_coefficient": 1.098,
        "density": 1.07982
    },
    {
        "salt": "LiBr",
        "molality": 1.6,
        "molarity": 1.5326932127078228,
        "num_particles": 102.07507260498566,
        "osmotic_coefficient": 1.13,
        "density": 1.09104
    },
    {
        "salt": "LiBr",
        "molality": 1.8,
        "molarity": 1.71564297457194,
        "num_particles": 114.25925275957249,
        "osmotic_coefficient": 1.163,
        "density": 1.10213
    },
    {
        "salt": "LiBr",
        "molality": 2.0,
        "molarity": 1.896735935383278,
        "num_particles": 126.31977274478952,
        "osmotic_coefficient": 1.196,
        "density": 1.11309
    },
    {
        "salt": "LiBr",
        "molality": 2.5,
        "molarity": 2.3415255368751864,
        "num_particles": 155.94209408724342,
        "osmotic_coefficient": 1.278,
        "density": 1.13996
    },
    {
        "salt": "LiBr",
        "molality": 3.0,
        "molarity": 2.7752025925499892,
        "num_particles": 184.82433652042673,
        "osmotic_coefficient": 1.364,
        "density": 1.16608
    },
    {
        "salt": "LiBr",
        "molality": 3.5,
        "molarity": 3.1981487126689325,
        "num_particles": 212.99191471623885,
        "osmotic_coefficient": 1.467,
        "density": 1.1915
    },
    {
        "salt": "LiBr",
        "molality": 4.0,
        "molarity": 3.6107408451958607,
        "num_particles": 240.4699328445546,
        "osmotic_coefficient": 1.578,
        "density": 1.21626
    },
    {
        "salt": "LiBr",
        "molality": 4.5,
        "molarity": 4.0132693175343,
        "num_particles": 267.2777262756545,
        "osmotic_coefficient": 1.687,
        "density": 1.24037
    },
    {
        "salt": "LiBr",
        "molality": 5.0,
        "molarity": 4.4061775523366284,
        "num_particles": 293.44482629411715,
        "osmotic_coefficient": 1.793,
        "density": 1.26389
    },
    {
        "salt": "LiBr",
        "molality": 5.5,
        "molarity": 4.789714732370204,
        "num_particles": 318.98782809907243,
        "osmotic_coefficient": 1.891,
        "density": 1.28682
    },
    {
        "salt": "LiBr",
        "molality": 6.0,
        "molarity": 5.1642593700487165,
        "num_particles": 343.93194005041204,
        "osmotic_coefficient": 1.989,
        "density": 1.3092
    },
    {
        "salt": "LiCl",
        "molality": 0.1,
        "molarity": 0.09953104807479173,
        "num_particles": 6.628618744083534,
        "osmotic_coefficient": 0.939,
        "density": 0.99953
    },
    {
        "salt": "LiCl",
        "molality": 0.2,
        "molarity": 0.19870918456590264,
        "num_particles": 13.233734105214312,
        "osmotic_coefficient": 0.939,
        "density": 1.00197
    },
    {
        "salt": "LiCl",
        "molality": 0.3,
        "molarity": 0.29752699220770396,
        "num_particles": 19.81485210460956,
        "osmotic_coefficient": 0.945,
        "density": 1.00437
    },
    {
        "salt": "LiCl",
        "molality": 0.4,
        "molarity": 0.3959850440175677,
        "num_particles": 26.372010904368093,
        "osmotic_coefficient": 0.954,
        "density": 1.00675
    },
    {
        "salt": "LiCl",
        "molality": 0.5,
        "molarity": 0.4940770487966573,
        "num_particles": 32.904791520069104,
        "osmotic_coefficient": 0.963,
        "density": 1.0091
    },
    {
        "salt": "LiCl",
        "molality": 0.6,
        "molarity": 0.5918046209399237,
        "num_particles": 39.41330146799861,
        "osmotic_coefficient": 0.973,
        "density": 1.01143
    },
    {
        "salt": "LiCl",
        "molality": 0.7,
        "molarity": 0.6891596364603305,
        "num_particles": 45.89699970278646,
        "osmotic_coefficient": 0.984,
        "density": 1.01373
    },
    {
        "salt": "LiCl",
        "molality": 0.8,
        "molarity": 0.786153448561352,
        "num_particles": 52.35664233078149,
        "osmotic_coefficient": 0.995,
        "density": 1.01602
    },
    {
        "salt": "LiCl",
        "molality": 0.9,
        "molarity": 0.8827702540642791,
        "num_particles": 58.79117688394851,
        "osmotic_coefficient": 1.006,
        "density": 1.01828
    },
    {
        "salt": "LiCl",
        "molality": 1.0,
        "molarity": 0.9790156121389801,
        "num_particles": 65.20097359467535,
        "osmotic_coefficient": 1.018,
        "density": 1.02052
    },
    {
        "salt": "LiCl",
        "molality": 1.2,
        "molarity": 1.1704213868700377,
        "num_particles": 77.94831154247555,
        "osmotic_coefficient": 1.041,
        "density": 1.02497
    },
    {
        "salt": "LiCl",
        "molality": 1.4,
        "molarity": 1.3602981295350853,
        "num_particles": 90.59381824455791,
        "osmotic_coefficient": 1.066,
        "density": 1.02931
    },
    {
        "salt": "LiCl",
        "molality": 1.6,
        "molarity": 1.5487103570005125,
        "num_particles": 103.14179042760351,
        "osmotic_coefficient": 1.091,
        "density": 1.0336
    },
    {
        "salt": "LiCl",
        "molality": 1.8,
        "molarity": 1.735631359464362,
        "num_particles": 115.5904492588026,
        "osmotic_coefficient": 1.116,
        "density": 1.03782
    },
    {
        "salt": "LiCl",
        "molality": 2.0,
        "molarity": 1.9210758231101377,
        "num_particles": 127.9407728159825,
        "osmotic_coefficient": 1.142,
        "density": 1.04198
    },
    {
        "salt": "LiCl",
        "molality": 2.5,
        "molarity": 2.378264623842096,
        "num_particles": 158.38886225878295,
        "osmotic_coefficient": 1.212,
        "density": 1.05213
    },
    {
        "salt": "LiCl",
        "molality": 3.0,
        "molarity": 2.8263315063583345,
        "num_particles": 188.22944560940118,
        "osmotic_coefficient": 1.286,
        "density": 1.06193
    },
    {
        "salt": "LiCl",
        "molality": 3.5,
        "molarity": 3.265415860094969,
        "num_particles": 217.4718059955329,
        "osmotic_coefficient": 1.366,
        "density": 1.07141
    },
    {
        "salt": "LiCl",
        "molality": 4.0,
        "molarity": 3.695732470570532,
        "num_particles": 246.13024781104954,
        "osmotic_coefficient": 1.449,
        "density": 1.08061
    },
    {
        "salt": "LiCl",
        "molality": 4.5,
        "molarity": 4.117510222351364,
        "num_particles": 274.2200144252919,
        "osmotic_coefficient": 1.533,
        "density": 1.08956
    },
    {
        "salt": "LiCl",
        "molality": 5.0,
        "molarity": 4.5309702385372566,
        "num_particles": 301.75583230555213,
        "osmotic_coefficient": 1.619,
        "density": 1.09828
    },
    {
        "salt": "LiCl",
        "molality": 5.5,
        "molarity": 4.936350875428876,
        "num_particles": 328.75357562449216,
        "osmotic_coefficient": 1.705,
        "density": 1.10679
    },
    {
        "salt": "LiCl",
        "molality": 6.0,
        "molarity": 5.333906266442596,
        "num_particles": 355.2301692870523,
        "osmotic_coefficient": 1.791,
        "density": 1.11511
    },
    {
        "salt": "LiClO4",
        "molality": 0.1,
        "molarity": 0.0992728362946611,
        "num_particles": 6.611422226224796,
        "osmotic_coefficient": 0.951,
        "density": 1.00329
    },
    {
        "salt": "LiClO4",
        "molality": 0.2,
        "molarity": 0.1976817281876237,
        "num_particles": 13.165307049139606,
        "osmotic_coefficient": 0.959,
        "density": 1.00944
    },
    {
        "salt": "LiClO4",
        "molality": 0.3,
        "molarity": 0.29523304684388374,
        "num_particles": 19.662078778791706,
        "osmotic_coefficient": 0.971,
        "density": 1.01552
    },
    {
        "salt": "LiClO4",
        "molality": 0.4,
        "molarity": 0.39193290336442366,
        "num_particles": 26.10214440535454,
        "osmotic_coefficient": 0.985,
        "density": 1.02153
    },
    {
        "salt": "LiClO4",
        "molality": 0.5,
        "molarity": 0.48779190938050404,
        "num_particles": 32.48621064757809,
        "osmotic_coefficient": 0.999,
        "density": 1.02748
    },
    {
        "salt": "LiClO4",
        "molality": 0.6,
        "molarity": 0.5828183720392466,
        "num_particles": 38.81483074901987,
        "osmotic_coefficient": 1.013,
        "density": 1.03337
    },
    {
        "salt": "LiClO4",
        "molality": 0.7,
        "molarity": 0.6770202694716385,
        "num_particles": 45.08853604125557,
        "osmotic_coefficient": 1.027,
        "density": 1.0392
    },
    {
        "salt": "LiClO4",
        "molality": 0.8,
        "molarity": 0.7704052669217554,
        "num_particles": 51.30783701806117,
        "osmotic_coefficient": 1.043,
        "density": 1.04497
    },
    {
        "salt": "LiClO4",
        "molality": 0.9,
        "molarity": 0.8629807319363616,
        "num_particles": 57.47322434701754,
        "osmotic_coefficient": 1.058,
        "density": 1.05068
    },
    {
        "salt": "LiClO4",
        "molality": 1.0,
        "molarity": 0.9547627870823128,
        "num_particles": 63.585771766932105,
        "osmotic_coefficient": 1.072,
        "density": 1.05634
    },
    {
        "salt": "LiClO4",
        "molality": 1.2,
        "molarity": 1.1359726444308076,
        "num_particles": 75.65407688645949,
        "osmotic_coefficient": 1.104,
        "density": 1.0675
    },
    {
        "salt": "LiClO4",
        "molality": 1.4,
        "molarity": 1.3140513131165437,
        "num_particles": 87.51384953031531,
        "osmotic_coefficient": 1.137,
        "density": 1.07841
    },
    {
        "salt": "LiClO4",
        "molality": 1.6,
        "molarity": 1.4891234498694268,
        "num_particles": 99.17339165002532,
        "osmotic_coefficient": 1.17,
        "density": 1.08913
    },
    {
        "salt": "LiClO4",
        "molality": 1.8,
        "molarity": 1.6612393432826802,
        "num_particles": 110.63605239058603,
        "osmotic_coefficient": 1.204,
        "density": 1.09965
    },
    {
        "salt": "LiClO4",
        "molality": 2.0,
        "molarity": 1.8304721383927838,
        "num_particles": 121.90670310188496,
        "osmotic_coefficient": 1.238,
        "density": 1.10998
    },
    {
        "salt": "LiClO4",
        "molality": 2.5,
        "molarity": 2.24125673887715,
        "num_particles": 149.26434230312609,
        "osmotic_coefficient": 1.328,
        "density": 1.13495
    },
    {
        "salt": "LiClO4",
        "molality": 3.0,
        "molarity": 2.635293404185965,
        "num_particles": 175.50659410338318,
        "osmotic_coefficient": 1.419,
        "density": 1.1588
    },
    {
        "salt": "LiClO4",
        "molality": 3.5,
        "molarity": 3.0134330152692614,
        "num_particles": 200.69012589964916,
        "osmotic_coefficient": 1.512,
        "density": 1.18158
    },
    {
        "salt": "LiClO4",
        "molality": 4.0,
        "molarity": 3.376553775358456,
        "num_particles": 224.87342471193924,
        "osmotic_coefficient": 1.595,
        "density": 1.20337
    },
    {
        "salt": "LiI",
        "molality": 0.1,
        "molarity": 0.09935019760505633,
        "num_particles": 6.616574373640819,
        "osmotic_coefficient": 0.952,
        "density": 1.0068
    },
    {
        "salt": "LiI",
        "molality": 0.2,
        "molarity": 0.19798981271365548,
        "num_particles": 13.185825017185937,
        "osmotic_coefficient": 0.966,
        "density": 1.01645
    },
    {
        "salt": "LiI",
        "molality": 0.3,
        "molarity": 0.2959232037532868,
        "num_particles": 19.708042195378965,
        "osmotic_coefficient": 0.98,
        "density": 1.02602
    },
    {
        "salt": "LiI",
        "molality": 0.4,
        "molarity": 0.3931583043833172,
        "num_particles": 26.183754278052287,
        "osmotic_coefficient": 0.995,
        "density": 1.03552
    },
    {
        "salt": "LiI",
        "molality": 0.5,
        "molarity": 0.48969234013637325,
        "num_particles": 32.61277648983388,
        "osmotic_coefficient": 1.008,
        "density": 1.04493
    },
    {
        "salt": "LiI",
        "molality": 0.6,
        "molarity": 0.5855374846108987,
        "num_particles": 38.99591957414891,
        "osmotic_coefficient": 1.022,
        "density": 1.05427
    },
    {
        "salt": "LiI",
        "molality": 0.7,
        "molarity": 0.6806998294771394,
        "num_particles": 45.33358922711287,
        "osmotic_coefficient": 1.034,
        "density": 1.06354
    },
    {
        "salt": "LiI",
        "molality": 0.8,
        "molarity": 0.7751851718033025,
        "num_particles": 51.62617152478666,
        "osmotic_coefficient": 1.049,
        "density": 1.07274
    },
    {
        "salt": "LiI",
        "molality": 0.9,
        "molarity": 0.8689909992726236,
        "num_particles": 57.87349915063623,
        "osmotic_coefficient": 1.063,
        "density": 1.08186
    },
    {
        "salt": "LiI",
        "molality": 1.0,
        "molarity": 0.962137848921815,
        "num_particles": 64.07693984055035,
        "osmotic_coefficient": 1.08,
        "density": 1.09092
    },
    {
        "salt": "LiI",
        "molality": 1.2,
        "molarity": 1.1464734366114662,
        "num_particles": 76.353413919705,
        "osmotic_coefficient": 1.111,
        "density": 1.10885
    },
    {
        "salt": "LiI",
        "molality": 1.4,
        "molarity": 1.3281954538946767,
        "num_particles": 88.45582812387374,
        "osmotic_coefficient": 1.143,
        "density": 1.12649
    },
    {
        "salt": "LiI",
        "molality": 1.6,
        "molarity": 1.5073861764512093,
        "num_particles": 100.3896618901127,
        "osmotic_coefficient": 1.176,
        "density": 1.14388
    },
    {
        "salt": "LiI",
        "molality": 1.8,
        "molarity": 1.6841030517434503,
        "num_particles": 112.15874113338351,
        "osmotic_coefficient": 1.212,
        "density": 1.16103
    },
    {
        "salt": "LiI",
        "molality": 2.0,
        "molarity": 1.8583892088033445,
        "num_particles": 123.76593818262366,
        "osmotic_coefficient": 1.25,
        "density": 1.17794
    },
    {
        "salt": "LiI",
        "molality": 2.5,
        "molarity": 2.283825044488152,
        "num_particles": 152.09932770652432,
        "osmotic_coefficient": 1.351,
        "density": 1.21922
    },
    {
        "salt": "LiI",
        "molality": 3.0,
        "molarity": 2.695173201098783,
        "num_particles": 179.494498901793,
        "osmotic_coefficient": 1.467,
        "density": 1.25914
    },
    {
        "salt": "LiNO3",
        "molality": 0.1,
        "molarity": 0.09941854887294062,
        "num_particles": 6.621126465719054,
        "osmotic_coefficient": 0.938,
        "density": 1.00104
    },
    {
        "salt": "LiNO3",
        "molality": 0.2,
        "molarity": 0.19826409671754247,
        "num_particles": 13.204091921077088,
        "osmotic_coefficient": 0.935,
        "density": 1.00499
    },
    {
        "salt": "LiNO3",
        "molality": 0.3,
        "molarity": 0.2965335591688631,
        "num_particles": 19.748690951988074,
        "osmotic_coefficient": 0.94,
        "density": 1.00889
    },
    {
        "salt": "LiNO3",
        "molality": 0.4,
        "molarity": 0.3942356125819694,
        "num_particles": 26.255501390705763,
        "osmotic_coefficient": 0.946,
        "density": 1.01277
    },
    {
        "salt": "LiNO3",
        "molality": 0.5,
        "molarity": 0.4913661352205423,
        "num_particles": 32.724248735764014,
        "osmotic_coefficient": 0.954,
        "density": 1.01661
    },
    {
        "salt": "LiNO3",
        "molality": 0.6,
        "molarity": 0.5879249556064544,
        "num_particles": 39.154921566976356,
        "osmotic_coefficient": 0.962,
        "density": 1.02041
    },
    {
        "salt": "LiNO3",
        "molality": 0.7,
        "molarity": 0.6839252622101608,
        "num_particles": 45.54839821672403,
        "osmotic_coefficient": 0.97,
        "density": 1.02419
    },
    {
        "salt": "LiNO3",
        "molality": 0.8,
        "molarity": 0.7793647351749049,
        "num_particles": 51.90452418602128,
        "osmotic_coefficient": 0.978,
        "density": 1.02794
    },
    {
        "salt": "LiNO3",
        "molality": 0.9,
        "molarity": 0.8742542969200926,
        "num_particles": 58.22402689164311,
        "osmotic_coefficient": 0.987,
        "density": 1.03167
    },
    {
        "salt": "LiNO3",
        "molality": 1.0,
        "molarity": 0.9685802650461298,
        "num_particles": 64.50599510626732,
        "osmotic_coefficient": 0.997,
        "density": 1.03536
    },
    {
        "salt": "LiNO3",
        "molality": 1.2,
        "molarity": 1.1556066524852984,
        "num_particles": 76.96167241899813,
        "osmotic_coefficient": 1.015,
        "density": 1.04268
    },
    {
        "salt": "LiNO3",
        "molality": 1.4,
        "molarity": 1.340420696520752,
        "num_particles": 89.27001097424699,
        "osmotic_coefficient": 1.033,
        "density": 1.04986
    },
    {
        "salt": "LiNO3",
        "molality": 1.6,
        "molarity": 1.5231012211324801,
        "num_particles": 101.43626033103442,
        "osmotic_coefficient": 1.052,
        "density": 1.05695
    },
    {
        "salt": "LiNO3",
        "molality": 1.8,
        "molarity": 1.7036626899248004,
        "num_particles": 113.4613837437473,
        "osmotic_coefficient": 1.07,
        "density": 1.06394
    },
    {
        "salt": "LiNO3",
        "molality": 2.0,
        "molarity": 1.8821294112270757,
        "num_particles": 125.34700011071702,
        "osmotic_coefficient": 1.088,
        "density": 1.07083
    },
    {
        "salt": "LiNO3",
        "molality": 2.5,
        "molarity": 2.319328877951832,
        "num_particles": 154.46382984466445,
        "osmotic_coefficient": 1.134,
        "density": 1.08764
    },
    {
        "salt": "LiNO3",
        "molality": 3.0,
        "molarity": 2.7440136952929883,
        "num_particles": 182.74720267160296,
        "osmotic_coefficient": 1.181,
        "density": 1.10386
    },
    {
        "salt": "LiNO3",
        "molality": 3.5,
        "molarity": 3.15662634102171,
        "num_particles": 210.2265869484376,
        "osmotic_coefficient": 1.227,
        "density": 1.11953
    },
    {
        "salt": "LiNO3",
        "molality": 4.0,
        "molarity": 3.557561468085506,
        "num_particles": 236.92826597044015,
        "osmotic_coefficient": 1.27,
        "density": 1.13467
    },
    {
        "salt": "LiNO3",
        "molality": 4.5,
        "molarity": 3.9472370687582665,
        "num_particles": 262.88007739706643,
        "osmotic_coefficient": 1.312,
        "density": 1.14931
    },
    {
        "salt": "LiNO3",
        "molality": 5.0,
        "molarity": 4.326035709770735,
        "num_particles": 288.10749959965204,
        "osmotic_coefficient": 1.352,
        "density": 1.16347
    },
    {
        "salt": "LiNO3",
        "molality": 5.5,
        "molarity": 4.6943307112876065,
        "num_particles": 312.6353951420814,
        "osmotic_coefficient": 1.387,
        "density": 1.17717
    },
    {
        "salt": "LiNO3",
        "molality": 6.0,
        "molarity": 5.052487274311795,
        "num_particles": 336.4880858642236,
        "osmotic_coefficient": 1.42,
        "density": 1.19043
    },
    {
        "salt": "NaBr",
        "molality": 0.1,
        "molarity": 0.0994655590764389,
        "num_particles": 6.624257274869559,
        "osmotic_coefficient": 0.934,
        "density": 1.00489
    },
    {
        "salt": "NaBr",
        "molality": 0.2,
        "molarity": 0.19844817470243353,
        "num_particles": 13.216351239195642,
        "osmotic_coefficient": 0.928,
        "density": 1.01266
    },
    {
        "salt": "NaBr",
        "molality": 0.3,
        "molarity": 0.29693902673494055,
        "num_particles": 19.775694484660605,
        "osmotic_coefficient": 0.928,
        "density": 1.02035
    },
    {
        "salt": "NaBr",
        "molality": 0.4,
        "molarity": 0.39494116932921586,
        "num_particles": 26.302490413430593,
        "osmotic_coefficient": 0.929,
        "density": 1.02799
    },
    {
        "salt": "NaBr",
        "molality": 0.5,
        "molarity": 0.4924451731756332,
        "num_particles": 32.79611104760583,
        "osmotic_coefficient": 0.933,
        "density": 1.03556
    },
    {
        "salt": "NaBr",
        "molality": 0.6,
        "molarity": 0.5894570441401462,
        "num_particles": 39.256956368864444,
        "osmotic_coefficient": 0.937,
        "density": 1.04308
    },
    {
        "salt": "NaBr",
        "molality": 0.7,
        "molarity": 0.6859769606291193,
        "num_particles": 45.68503825880311,
        "osmotic_coefficient": 0.942,
        "density": 1.05055
    },
    {
        "salt": "NaBr",
        "molality": 0.8,
        "molarity": 0.7819977027025029,
        "num_particles": 52.079875880227135,
        "osmotic_coefficient": 0.947,
        "density": 1.05796
    },
    {
        "salt": "NaBr",
        "molality": 0.9,
        "molarity": 0.8775251358085076,
        "num_particles": 58.44185986320323,
        "osmotic_coefficient": 0.953,
        "density": 1.06532
    },
    {
        "salt": "NaBr",
        "molality": 1.0,
        "molarity": 0.9725594662769041,
        "num_particles": 64.77100394898513,
        "osmotic_coefficient": 0.958,
        "density": 1.07263
    },
    {
        "salt": "NaBr",
        "molality": 1.2,
        "molarity": 1.1611709691592,
        "num_particles": 77.33224757635932,
        "osmotic_coefficient": 0.969,
        "density": 1.08712
    },
    {
        "salt": "NaBr",
        "molality": 1.4,
        "molarity": 1.347781865782977,
        "num_particles": 89.76025382302409,
        "osmotic_coefficient": 0.983,
        "density": 1.10138
    },
    {
        "salt": "NaBr",
        "molality": 1.6,
        "molarity": 1.5324621442133057,
        "num_particles": 102.059683789299,
        "osmotic_coefficient": 0.997,
        "density": 1.11547
    },
    {
        "salt": "NaBr",
        "molality": 1.8,
        "molarity": 1.7151959333424007,
        "num_particles": 114.22948048317414,
        "osmotic_coefficient": 1.012,
        "density": 1.12937
    },
    {
        "salt": "NaBr",
        "molality": 2.0,
        "molarity": 1.8960049361911049,
        "num_particles": 126.27108929333517,
        "osmotic_coefficient": 1.028,
        "density": 1.14309
    },
    {
        "salt": "NaBr",
        "molality": 2.5,
        "molarity": 2.3396978289659445,
        "num_particles": 155.8203714776633,
        "osmotic_coefficient": 1.067,
        "density": 1.17662
    },
    {
        "salt": "NaBr",
        "molality": 3.0,
        "molarity": 2.771719944188123,
        "num_particles": 184.5923973551406,
        "osmotic_coefficient": 1.107,
        "density": 1.2091
    },
    {
        "salt": "NaBr",
        "molality": 3.5,
        "molarity": 3.1923920451663044,
        "num_particles": 212.60852928174904,
        "osmotic_coefficient": 1.15,
        "density": 1.24059
    },
    {
        "salt": "NaBr",
        "molality": 4.0,
        "molarity": 3.602016469534761,
        "num_particles": 239.88890249115036,
        "osmotic_coefficient": 1.199,
        "density": 1.27113
    },
    {
        "salt": "NaCl",
        "molality": 0.1,
        "molarity": 0.09953432142558886,
        "num_particles": 6.6288367443444525,
        "osmotic_coefficient": 0.932,
        "density": 1.00116
    },
    {
        "salt": "NaCl",
        "molality": 0.2,
        "molarity": 0.19871739113244402,
        "num_particles": 13.234280650255815,
        "osmotic_coefficient": 0.925,
        "density": 1.0052
    },
    {
        "salt": "NaCl",
        "molality": 0.3,
        "molarity": 0.29754641623064426,
        "num_particles": 19.816145715447966,
        "osmotic_coefficient": 0.922,
        "density": 1.00921
    },
    {
        "salt": "NaCl",
        "molality": 0.4,
        "molarity": 0.3960108503619393,
        "num_particles": 26.373729568255662,
        "osmotic_coefficient": 0.92,
        "density": 1.01317
    },
    {
        "salt": "NaCl",
        "molality": 0.5,
        "molarity": 0.4941071879675871,
        "num_particles": 32.90679874371661,
        "osmotic_coefficient": 0.921,
        "density": 1.01709
    },
    {
        "salt": "NaCl",
        "molality": 0.6,
        "molarity": 0.5918358671541083,
        "num_particles": 39.41538241906897,
        "osmotic_coefficient": 0.923,
        "density": 1.02098
    },
    {
        "salt": "NaCl",
        "molality": 0.7,
        "molarity": 0.689187709192359,
        "num_particles": 45.89886930469783,
        "osmotic_coefficient": 0.926,
        "density": 1.02483
    },
    {
        "salt": "NaCl",
        "molality": 0.8,
        "molarity": 0.7861728470545077,
        "num_particles": 52.35793424137448,
        "osmotic_coefficient": 0.929,
        "density": 1.02866
    },
    {
        "salt": "NaCl",
        "molality": 0.9,
        "molarity": 0.8827745877810671,
        "num_particles": 58.79146550299642,
        "osmotic_coefficient": 0.932,
        "density": 1.03245
    },
    {
        "salt": "NaCl",
        "molality": 1.0,
        "molarity": 0.9789973923887986,
        "num_particles": 65.19976018659916,
        "osmotic_coefficient": 0.936,
        "density": 1.03621
    },
    {
        "salt": "NaCl",
        "molality": 1.2,
        "molarity": 1.1703198122093807,
        "num_particles": 77.94154682219401,
        "osmotic_coefficient": 0.943,
        "density": 1.04366
    },
    {
        "salt": "NaCl",
        "molality": 1.4,
        "molarity": 1.3600686253484882,
        "num_particles": 90.578533609436,
        "osmotic_coefficient": 0.951,
        "density": 1.05096
    },
    {
        "salt": "NaCl",
        "molality": 1.6,
        "molarity": 1.5482997775956928,
        "num_particles": 103.11444645412624,
        "osmotic_coefficient": 0.962,
        "density": 1.05817
    },
    {
        "salt": "NaCl",
        "molality": 1.8,
        "molarity": 1.734979985378106,
        "num_particles": 115.54706872015579,
        "osmotic_coefficient": 0.972,
        "density": 1.06527
    },
    {
        "salt": "NaCl",
        "molality": 2.0,
        "molarity": 1.9201167538141968,
        "num_particles": 127.87690023717502,
        "osmotic_coefficient": 0.983,
        "density": 1.07227
    },
    {
        "salt": "NaCl",
        "molality": 2.5,
        "molarity": 2.376145188028968,
        "num_particles": 158.2477110076957,
        "osmotic_coefficient": 1.013,
        "density": 1.08932
    },
    {
        "salt": "NaCl",
        "molality": 3.0,
        "molarity": 2.822524929380935,
        "num_particles": 187.97593328343606,
        "osmotic_coefficient": 1.045,
        "density": 1.10579
    },
    {
        "salt": "NaCl",
        "molality": 3.5,
        "molarity": 3.259294004350208,
        "num_particles": 217.06409957102298,
        "osmotic_coefficient": 1.08,
        "density": 1.1217
    },
    {
        "salt": "NaCl",
        "molality": 4.0,
        "molarity": 3.686584100635456,
        "num_particles": 245.5209800739723,
        "osmotic_coefficient": 1.116,
        "density": 1.13709
    },
    {
        "salt": "NaCl",
        "molality": 4.5,
        "molarity": 4.104542431392421,
        "num_particles": 273.35637896799005,
        "osmotic_coefficient": 1.153,
        "density": 1.15199
    },
    {
        "salt": "NaCl",
        "molality": 5.0,
        "molarity": 4.513388020430273,
        "num_particles": 300.5848829107569,
        "osmotic_coefficient": 1.192,
        "density": 1.16644
    },
    {
        "salt": "NaCl",
        "molality": 5.5,
        "molarity": 4.913381059769036,
        "num_particles": 327.2238203011428,
        "osmotic_coefficient": 1.231,
        "density": 1.18048
    },
    {
        "salt": "NaCl",
        "molality": 6.0,
        "molarity": 5.304685186282059,
        "num_particles": 353.28408910985024,
        "osmotic_coefficient": 1.271,
        "density": 1.19412
    },
    {
        "salt": "NaI",
        "molality": 0.1,
        "molarity": 0.09935280086779266,
        "num_particles": 6.616747747040413,
        "osmotic_coefficient": 0.938,
        "density": 1.00842
    },
    {
        "salt": "NaI",
        "molality": 0.2,
        "molarity": 0.1980003456384505,
        "num_particles": 13.186526494203177,
        "osmotic_coefficient": 0.936,
        "density": 1.01968
    },
    {
        "salt": "NaI",
        "molality": 0.3,
        "molarity": 0.29594427383831257,
        "num_particles": 19.70944543148712,
        "osmotic_coefficient": 0.939,
        "density": 1.03084
    },
    {
        "salt": "NaI",
        "molality": 0.4,
        "molarity": 0.3931861322545465,
        "num_particles": 26.18560757260114,
        "osmotic_coefficient": 0.945,
        "density": 1.0419
    },
    {
        "salt": "NaI",
        "molality": 0.5,
        "molarity": 0.4897320328016783,
        "num_particles": 32.61541996189946,
        "osmotic_coefficient": 0.952,
        "density": 1.05287
    },
    {
        "salt": "NaI",
        "molality": 0.6,
        "molarity": 0.5855804112909588,
        "num_particles": 38.998778426753915,
        "osmotic_coefficient": 0.959,
        "density": 1.06374
    },
    {
        "salt": "NaI",
        "molality": 0.7,
        "molarity": 0.6807388388150123,
        "num_particles": 45.33618719059481,
        "osmotic_coefficient": 0.967,
        "density": 1.07452
    },
    {
        "salt": "NaI",
        "molality": 0.8,
        "molarity": 0.7752180528470094,
        "num_particles": 51.62836135305489,
        "osmotic_coefficient": 0.975,
        "density": 1.08522
    },
    {
        "salt": "NaI",
        "molality": 0.9,
        "molarity": 0.869007957522286,
        "num_particles": 57.874628544667075,
        "osmotic_coefficient": 0.983,
        "density": 1.09582
    },
    {
        "salt": "NaI",
        "molality": 1.0,
        "molarity": 0.962126812129856,
        "num_particles": 64.07620480673458,
        "osmotic_coefficient": 0.991,
        "density": 1.10634
    },
    {
        "salt": "NaI",
        "molality": 1.2,
        "molarity": 1.1463621354253188,
        "num_particles": 76.34600142739224,
        "osmotic_coefficient": 1.007,
        "density": 1.12713
    },
    {
        "salt": "NaI",
        "molality": 1.4,
        "molarity": 1.327924380458339,
        "num_particles": 88.43777503897323,
        "osmotic_coefficient": 1.025,
        "density": 1.14756
    },
    {
        "salt": "NaI",
        "molality": 1.6,
        "molarity": 1.5068848481719985,
        "num_particles": 100.35627417750649,
        "osmotic_coefficient": 1.043,
        "density": 1.16767
    },
    {
        "salt": "NaI",
        "molality": 1.8,
        "molarity": 1.6832907807673956,
        "num_particles": 112.10464510283529,
        "osmotic_coefficient": 1.061,
        "density": 1.18747
    },
    {
        "salt": "NaI",
        "molality": 2.0,
        "molarity": 1.857175829755805,
        "num_particles": 123.685128955214,
        "osmotic_coefficient": 1.079,
        "density": 1.20696
    },
    {
        "salt": "NaI",
        "molality": 2.5,
        "molarity": 2.2811471385186133,
        "num_particles": 151.92098317938505,
        "osmotic_coefficient": 1.129,
        "density": 1.25438
    },
    {
        "salt": "NaI",
        "molality": 3.0,
        "molarity": 2.6903088289058883,
        "num_particles": 179.17053899863,
        "osmotic_coefficient": 1.188,
        "density": 1.30002
    },
    {
        "salt": "NaI",
        "molality": 3.5,
        "molarity": 3.0853461365656245,
        "num_particles": 205.47943208089652,
        "osmotic_coefficient": 1.243,
        "density": 1.34399
    },
    {
        "salt": "NaNO3",
        "molality": 0.1,
        "molarity": 0.0994189912663018,
        "num_particles": 6.621155928454381,
        "osmotic_coefficient": 0.921,
        "density": 1.00264
    },
    {
        "salt": "NaNO3",
        "molality": 0.2,
        "molarity": 0.19825979366310847,
        "num_particles": 13.203805344096036,
        "osmotic_coefficient": 0.902,
        "density": 1.00815
    },
    {
        "salt": "NaNO3",
        "molality": 0.3,
        "molarity": 0.296516305666432,
        "num_particles": 19.74754189456501,
        "osmotic_coefficient": 0.89,
        "density": 1.01359
    },
    {
        "salt": "NaNO3",
        "molality": 0.4,
        "molarity": 0.3941826263705686,
        "num_particles": 26.25197258837862,
        "osmotic_coefficient": 0.881,
        "density": 1.01896
    },
    {
        "salt": "NaNO3",
        "molality": 0.5,
        "molarity": 0.491262639660427,
        "num_particles": 32.71735608645529,
        "osmotic_coefficient": 0.873,
        "density": 1.02428
    },
    {
        "salt": "NaNO3",
        "molality": 0.6,
        "molarity": 0.5877562978734797,
        "num_particles": 39.14368921454206,
        "osmotic_coefficient": 0.867,
        "density": 1.02955
    },
    {
        "salt": "NaNO3",
        "molality": 0.7,
        "molarity": 0.6836569479634514,
        "num_particles": 45.53052888972061,
        "osmotic_coefficient": 0.862,
        "density": 1.03476
    },
    {
        "salt": "NaNO3",
        "molality": 0.8,
        "molarity": 0.7789693846724635,
        "num_particles": 51.87819443463559,
        "osmotic_coefficient": 0.858,
        "density": 1.03992
    },
    {
        "salt": "NaNO3",
        "molality": 0.9,
        "molarity": 0.8737019670769929,
        "num_particles": 58.18724255126184,
        "osmotic_coefficient": 0.854,
        "density": 1.04504
    },
    {
        "salt": "NaNO3",
        "molality": 1.0,
        "molarity": 0.9678480457093479,
        "num_particles": 64.45723039500933,
        "osmotic_coefficient": 0.851,
        "density": 1.05011
    },
    {
        "salt": "NaNO3",
        "molality": 1.2,
        "molarity": 1.1544131960688995,
        "num_particles": 76.88219000898629,
        "osmotic_coefficient": 0.845,
        "density": 1.06013
    },
    {
        "salt": "NaNO3",
        "molality": 1.4,
        "molarity": 1.3386290729470247,
        "num_particles": 89.15069152737222,
        "osmotic_coefficient": 0.839,
        "density": 1.06994
    },
    {
        "salt": "NaNO3",
        "molality": 1.6,
        "molarity": 1.520574731050809,
        "num_particles": 101.26799987526668,
        "osmotic_coefficient": 0.835,
        "density": 1.0796
    },
    {
        "salt": "NaNO3",
        "molality": 1.8,
        "molarity": 1.7002413012159703,
        "num_particles": 113.23352437961094,
        "osmotic_coefficient": 0.83,
        "density": 1.08909
    },
    {
        "salt": "NaNO3",
        "molality": 2.0,
        "molarity": 1.877658036901873,
        "num_particles": 125.0492132769887,
        "osmotic_coefficient": 0.826,
        "density": 1.09842
    },
    {
        "salt": "NaNO3",
        "molality": 2.5,
        "molarity": 2.311489177098224,
        "num_particles": 153.9417175085501,
        "osmotic_coefficient": 0.817,
        "density": 1.12106
    },
    {
        "salt": "NaNO3",
        "molality": 3.0,
        "molarity": 2.7317318203473655,
        "num_particles": 181.92924819356043,
        "osmotic_coefficient": 0.81,
        "density": 1.14276
    },
    {
        "salt": "NaNO3",
        "molality": 3.5,
        "molarity": 3.1387423689178755,
        "num_particles": 209.03554118935887,
        "osmotic_coefficient": 0.804,
        "density": 1.16356
    },
    {
        "salt": "NaNO3",
        "molality": 4.0,
        "molarity": 3.5328917144062286,
        "num_particles": 235.2852973208234,
        "osmotic_coefficient": 0.797,
        "density": 1.1835
    },
    {
        "salt": "NaNO3",
        "molality": 4.5,
        "molarity": 3.9145304604350675,
        "num_particles": 260.701866264158,
        "osmotic_coefficient": 0.792,
        "density": 1.20261
    },
    {
        "salt": "NaNO3",
        "molality": 5.0,
        "molarity": 4.284009492106344,
        "num_particles": 285.3086164416672,
        "osmotic_coefficient": 0.788,
        "density": 1.22092
    },
    {
        "salt": "NaNO3",
        "molality": 5.5,
        "molarity": 4.641642455793926,
        "num_particles": 309.12643623213376,
        "osmotic_coefficient": 0.787,
        "density": 1.23845
    },
    {
        "salt": "NaNO3",
        "molality": 6.0,
        "molarity": 4.9878533865812535,
        "num_particles": 332.1835657370798,
        "osmotic_coefficient": 0.788,
        "density": 1.25525
    },
    {
        "salt": "RbBr",
        "molality": 0.1,
        "molarity": 0.09931461435941549,
        "num_particles": 6.614204582770609,
        "osmotic_coefficient": 0.922,
        "density": 1.00957
    },
    {
        "salt": "RbBr",
        "molality": 0.2,
        "molarity": 0.19784828662872683,
        "num_particles": 13.176399591879154,
        "osmotic_coefficient": 0.904,
        "density": 1.02196
    },
    {
        "salt": "RbBr",
        "molality": 0.3,
        "molarity": 0.2955979145047559,
        "num_particles": 19.686378418579984,
        "osmotic_coefficient": 0.896,
        "density": 1.03421
    },
    {
        "salt": "RbBr",
        "molality": 0.4,
        "molarity": 0.3925680918085731,
        "num_particles": 26.144447004476678,
        "osmotic_coefficient": 0.89,
        "density": 1.04634
    },
    {
        "salt": "RbBr",
        "molality": 0.5,
        "molarity": 0.4887659025793259,
        "num_particles": 32.55107713596741,
        "osmotic_coefficient": 0.886,
        "density": 1.05836
    },
    {
        "salt": "RbBr",
        "molality": 0.6,
        "molarity": 0.5841852682876417,
        "num_particles": 38.90586399209916,
        "osmotic_coefficient": 0.884,
        "density": 1.07025
    },
    {
        "salt": "RbBr",
        "molality": 0.7,
        "molarity": 0.6788383957702745,
        "num_particles": 45.20962052991878,
        "osmotic_coefficient": 0.881,
        "density": 1.08203
    },
    {
        "salt": "RbBr",
        "molality": 0.8,
        "molarity": 0.7727297134604895,
        "num_particles": 51.46264167644973,
        "osmotic_coefficient": 0.88,
        "density": 1.0937
    },
    {
        "salt": "RbBr",
        "molality": 0.9,
        "molarity": 0.8658633948066334,
        "num_particles": 57.665205377101735,
        "osmotic_coefficient": 0.879,
        "density": 1.10526
    },
    {
        "salt": "RbBr",
        "molality": 1.0,
        "molarity": 0.9582433763639421,
        "num_particles": 63.81757380055811,
        "osmotic_coefficient": 0.878,
        "density": 1.11671
    },
    {
        "salt": "RbBr",
        "molality": 1.2,
        "molarity": 1.1407869388234635,
        "num_particles": 75.9747016831231,
        "osmotic_coefficient": 0.878,
        "density": 1.13931
    },
    {
        "salt": "RbBr",
        "molality": 1.4,
        "molarity": 1.3203431074814167,
        "num_particles": 87.9328736124246,
        "osmotic_coefficient": 0.878,
        "density": 1.16145
    },
    {
        "salt": "RbBr",
        "molality": 1.6,
        "molarity": 1.4970165947174243,
        "num_particles": 99.69906327612823,
        "osmotic_coefficient": 0.88,
        "density": 1.1832
    },
    {
        "salt": "RbBr",
        "molality": 1.8,
        "molarity": 1.6708336235972545,
        "num_particles": 111.27501709114247,
        "osmotic_coefficient": 0.882,
        "density": 1.20455
    },
    {
        "salt": "RbBr",
        "molality": 2.0,
        "molarity": 1.8418418568860726,
        "num_particles": 122.66390932624759,
        "osmotic_coefficient": 0.886,
        "density": 1.22551
    },
    {
        "salt": "RbBr",
        "molality": 2.5,
        "molarity": 2.257451730895764,
        "num_particles": 150.34290451794573,
        "osmotic_coefficient": 0.893,
        "density": 1.2763
    },
    {
        "salt": "RbBr",
        "molality": 3.0,
        "molarity": 2.656658975640926,
        "num_particles": 176.9295091652038,
        "osmotic_coefficient": 0.901,
        "density": 1.32489
    },
    {
        "salt": "RbBr",
        "molality": 3.5,
        "molarity": 3.040327412810473,
        "num_particles": 202.4812524988441,
        "osmotic_coefficient": 0.911,
        "density": 1.37145
    },
    {
        "salt": "RbBr",
        "molality": 4.0,
        "molarity": 3.409257244108895,
        "num_particles": 227.05142675400367,
        "osmotic_coefficient": 0.921,
        "density": 1.41611
    },
    {
        "salt": "RbBr",
        "molality": 4.5,
        "molarity": 3.764323398926942,
        "num_particles": 250.69830091781216,
        "osmotic_coefficient": 0.931,
        "density": 1.45903
    },
    {
        "salt": "RbBr",
        "molality": 5.0,
        "molarity": 4.106362830211401,
        "num_particles": 273.4776148031048,
        "osmotic_coefficient": 0.94,
        "density": 1.50035
    },
    {
        "salt": "RbCl",
        "molality": 0.1,
        "molarity": 0.09938324782892782,
        "num_particles": 6.618775469054645,
        "osmotic_coefficient": 0.923,
        "density": 1.00585
    },
    {
        "salt": "RbCl",
        "molality": 0.2,
        "molarity": 0.19811475318599917,
        "num_particles": 13.194145865533175,
        "osmotic_coefficient": 0.907,
        "density": 1.01453
    },
    {
        "salt": "RbCl",
        "molality": 0.3,
        "molarity": 0.2961912763999331,
        "num_particles": 19.72589543218001,
        "osmotic_coefficient": 0.898,
        "density": 1.02312
    },
    {
        "salt": "RbCl",
        "molality": 0.4,
        "molarity": 0.393613542720288,
        "num_particles": 26.214072469529604,
        "osmotic_coefficient": 0.893,
        "density": 1.03163
    },
    {
        "salt": "RbCl",
        "molality": 0.5,
        "molarity": 0.4903765863980789,
        "num_particles": 32.65834626613627,
        "osmotic_coefficient": 0.889,
        "density": 1.04005
    },
    {
        "salt": "RbCl",
        "molality": 0.6,
        "molarity": 0.5864887185952465,
        "num_particles": 39.05927033293846,
        "osmotic_coefficient": 0.887,
        "density": 1.0484
    },
    {
        "salt": "RbCl",
        "molality": 0.7,
        "molarity": 0.6819458943560043,
        "num_particles": 45.416575281938506,
        "osmotic_coefficient": 0.886,
        "density": 1.05667
    },
    {
        "salt": "RbCl",
        "molality": 0.8,
        "molarity": 0.776747894298796,
        "num_particles": 51.730246502653316,
        "osmotic_coefficient": 0.886,
        "density": 1.06486
    },
    {
        "salt": "RbCl",
        "molality": 0.9,
        "molarity": 0.8709026252833056,
        "num_particles": 58.00081058009654,
        "osmotic_coefficient": 0.885,
        "density": 1.07298
    },
    {
        "salt": "RbCl",
        "molality": 1.0,
        "molarity": 0.9644212214776955,
        "num_particles": 64.22900903319325,
        "osmotic_coefficient": 0.885,
        "density": 1.08104
    },
    {
        "salt": "RbCl",
        "molality": 1.2,
        "molarity": 1.1495363046120128,
        "num_particles": 76.55739634159028,
        "osmotic_coefficient": 0.886,
        "density": 1.09695
    },
    {
        "salt": "RbCl",
        "molality": 1.4,
        "molarity": 1.332065440771121,
        "num_particles": 88.71356345415258,
        "osmotic_coefficient": 0.888,
        "density": 1.11255
    },
    {
        "salt": "RbCl",
        "molality": 1.6,
        "molarity": 1.5121038286896333,
        "num_particles": 100.70385046403575,
        "osmotic_coefficient": 0.89,
        "density": 1.12791
    },
    {
        "salt": "RbCl",
        "molality": 1.8,
        "molarity": 1.6896520516683755,
        "num_particles": 112.52829621820125,
        "osmotic_coefficient": 0.893,
        "density": 1.14301
    },
    {
        "salt": "RbCl",
        "molality": 2.0,
        "molarity": 1.864729973700358,
        "num_particles": 124.18822362883525,
        "osmotic_coefficient": 0.896,
        "density": 1.15785
    },
    {
        "salt": "RbCl",
        "molality": 2.5,
        "molarity": 2.2919214237859484,
        "num_particles": 152.63853444261994,
        "osmotic_coefficient": 0.905,
        "density": 1.19391
    },
    {
        "salt": "RbCl",
        "molality": 3.0,
        "molarity": 2.704476126810018,
        "num_particles": 180.11405982209973,
        "osmotic_coefficient": 0.916,
        "density": 1.22852
    },
    {
        "salt": "RbCl",
        "molality": 3.5,
        "molarity": 3.1029279659870714,
        "num_particles": 206.65035558981714,
        "osmotic_coefficient": 0.928,
        "density": 1.26176
    },
    {
        "salt": "RbCl",
        "molality": 4.0,
        "molarity": 3.4877777208623937,
        "num_particles": 232.2807729135207,
        "osmotic_coefficient": 0.941,
        "density": 1.29369
    },
    {
        "salt": "RbCl",
        "molality": 4.5,
        "molarity": 3.8595545947934276,
        "num_particles": 257.04055594428115,
        "osmotic_coefficient": 0.952,
        "density": 1.32438
    },
    {
        "salt": "RbCl",
        "molality": 5.0,
        "molarity": 4.218826440151937,
        "num_particles": 280.96752279964227,
        "osmotic_coefficient": 0.966,
        "density": 1.35391
    },
    {
        "salt": "RbNO3",
        "molality": 0.1,
        "molarity": 0.09927102047968002,
        "num_particles": 6.611301295666419,
        "osmotic_coefficient": 0.903,
        "density": 1.00735
    },
    {
        "salt": "RbNO3",
        "molality": 0.2,
        "molarity": 0.19766980807864368,
        "num_particles": 13.164513187733093,
        "osmotic_coefficient": 0.871,
        "density": 1.0175
    },
    {
        "salt": "RbNO3",
        "molality": 0.3,
        "molarity": 0.2951930965420943,
        "num_particles": 19.659418148522104,
        "osmotic_coefficient": 0.847,
        "density": 1.02751
    },
    {
        "salt": "RbNO3",
        "molality": 0.4,
        "molarity": 0.39184913311674946,
        "num_particles": 26.096565432313763,
        "osmotic_coefficient": 0.826,
        "density": 1.03741
    },
    {
        "salt": "RbNO3",
        "molality": 0.5,
        "molarity": 0.48763826134251753,
        "num_particles": 32.47597791835149,
        "osmotic_coefficient": 0.809,
        "density": 1.04719
    },
    {
        "salt": "RbNO3",
        "molality": 0.6,
        "molarity": 0.5825626435597847,
        "num_particles": 38.797799615266676,
        "osmotic_coefficient": 0.794,
        "density": 1.05685
    },
    {
        "salt": "RbNO3",
        "molality": 0.7,
        "molarity": 0.6766370164872981,
        "num_particles": 45.06301196645817,
        "osmotic_coefficient": 0.781,
        "density": 1.06641
    },
    {
        "salt": "RbNO3",
        "molality": 0.8,
        "molarity": 0.7698538719531612,
        "num_particles": 51.27111493892191,
        "osmotic_coefficient": 0.768,
        "density": 1.07585
    },
    {
        "salt": "RbNO3",
        "molality": 0.9,
        "molarity": 0.8622387573619986,
        "num_particles": 57.4238099515461,
        "osmotic_coefficient": 0.756,
        "density": 1.0852
    },
    {
        "salt": "RbNO3",
        "molality": 1.0,
        "molarity": 0.9537827905318907,
        "num_particles": 63.520505464316834,
        "osmotic_coefficient": 0.745,
        "density": 1.09444
    },
    {
        "salt": "RbNO3",
        "molality": 1.2,
        "molarity": 1.1344237513420081,
        "num_particles": 75.55092292636775,
        "osmotic_coefficient": 0.725,
        "density": 1.11265
    },
    {
        "salt": "RbNO3",
        "molality": 1.4,
        "molarity": 1.3117824992776397,
        "num_particles": 87.36274992641991,
        "osmotic_coefficient": 0.706,
        "density": 1.13044
    },
    {
        "salt": "RbNO3",
        "molality": 1.6,
        "molarity": 1.4859807397799019,
        "num_particles": 98.96409186458558,
        "osmotic_coefficient": 0.689,
        "density": 1.14788
    },
    {
        "salt": "RbNO3",
        "molality": 1.8,
        "molarity": 1.6570877396002723,
        "num_particles": 110.35956180277933,
        "osmotic_coefficient": 0.673,
        "density": 1.16498
    },
    {
        "salt": "RbNO3",
        "molality": 2.0,
        "molarity": 1.82515718802174,
        "num_particles": 121.55273536684314,
        "osmotic_coefficient": 0.656,
        "density": 1.18174
    },
    {
        "salt": "RbNO3",
        "molality": 2.5,
        "molarity": 2.2325667201852877,
        "num_particles": 148.68560007242002,
        "osmotic_coefficient": 0.62,
        "density": 1.22227
    },
    {
        "salt": "RbNO3",
        "molality": 3.0,
        "molarity": 2.6226983976223273,
        "num_particles": 174.66778552852674,
        "osmotic_coefficient": 0.588,
        "density": 1.26101
    },
    {
        "salt": "RbNO3",
        "molality": 3.5,
        "molarity": 2.996717684960415,
        "num_particles": 199.5769099339587,
        "osmotic_coefficient": 0.561,
        "density": 1.29814
    },
    {
        "salt": "RbNO3",
        "molality": 4.0,
        "molarity": 3.355850586077545,
        "num_particles": 223.4946233109268,
        "osmotic_coefficient": 0.538,
        "density": 1.33386
    },
    {
        "salt": "RbNO3",
        "molality": 4.5,
        "molarity": 3.70129208534237,
        "num_particles": 246.50050982877488,
        "osmotic_coefficient": 0.516,
        "density": 1.36835
    },
    {
        "salt": "NH4Cl",
        "molality": 0.1,
        "molarity": 0.0993436011431253,
        "num_particles": 6.6161350591550745,
        "osmotic_coefficient": 0.927,
        "density": 0.99875
    },
    {
        "salt": "NH4Cl",
        "molality": 0.2,
        "molarity": 0.1979641400370556,
        "num_particles": 13.184115255371786,
        "osmotic_coefficient": 0.913,
        "density": 1.00041
    },
    {
        "salt": "NH4Cl",
        "molality": 0.3,
        "molarity": 0.2958582735272265,
        "num_particles": 19.703717939562853,
        "osmotic_coefficient": 0.906,
        "density": 1.00202
    },
    {
        "salt": "NH4Cl",
        "molality": 0.4,
        "molarity": 0.3930305609066177,
        "num_particles": 26.175246753812733,
        "osmotic_coefficient": 0.901,
        "density": 1.0036
    },
    {
        "salt": "NH4Cl",
        "molality": 0.5,
        "molarity": 0.4894835185545007,
        "num_particles": 32.598869285212366,
        "osmotic_coefficient": 0.899,
        "density": 1.00515
    },
    {
        "salt": "NH4Cl",
        "molality": 0.6,
        "molarity": 0.5852254241035657,
        "num_particles": 38.97513681170235,
        "osmotic_coefficient": 0.897,
        "density": 1.00668
    },
    {
        "salt": "NH4Cl",
        "molality": 0.7,
        "molarity": 0.680254745390039,
        "num_particles": 45.30394729346991,
        "osmotic_coefficient": 0.896,
        "density": 1.00818
    },
    {
        "salt": "NH4Cl",
        "molality": 0.8,
        "molarity": 0.774581489246953,
        "num_particles": 51.58596717060879,
        "osmotic_coefficient": 0.896,
        "density": 1.00966
    },
    {
        "salt": "NH4Cl",
        "molality": 0.9,
        "molarity": 0.868202101261289,
        "num_particles": 57.820959724535015,
        "osmotic_coefficient": 0.896,
        "density": 1.01111
    },
    {
        "salt": "NH4Cl",
        "molality": 1.0,
        "molarity": 0.9611377790602862,
        "num_particles": 64.01033668547716,
        "osmotic_coefficient": 0.897,
        "density": 1.01255
    },
    {
        "salt": "NH4Cl",
        "molality": 1.2,
        "molarity": 1.1449618169400704,
        "num_particles": 76.25274231339166,
        "osmotic_coefficient": 0.898,
        "density": 1.01538
    },
    {
        "salt": "NH4Cl",
        "molality": 1.4,
        "molarity": 1.3260365690396965,
        "num_particles": 88.312049625678,
        "osmotic_coefficient": 0.9,
        "density": 1.0181
    },
    {
        "salt": "NH4Cl",
        "molality": 1.6,
        "molarity": 1.5044709509779792,
        "num_particles": 100.19551223943725,
        "osmotic_coefficient": 0.903,
        "density": 1.02077
    },
    {
        "salt": "NH4Cl",
        "molality": 1.8,
        "molarity": 1.6802820583502192,
        "num_particles": 111.90426869571402,
        "osmotic_coefficient": 0.906,
        "density": 1.02337
    },
    {
        "salt": "NH4Cl",
        "molality": 2.0,
        "molarity": 1.8535441407358024,
        "num_particles": 123.44326390529929,
        "osmotic_coefficient": 0.909,
        "density": 1.02592
    },
    {
        "salt": "NH4Cl",
        "molality": 2.5,
        "molarity": 2.275701171577827,
        "num_particles": 151.55828993700874,
        "osmotic_coefficient": 0.918,
        "density": 1.03201
    },
    {
        "salt": "NH4Cl",
        "molality": 3.0,
        "molarity": 2.682768147126215,
        "num_particles": 178.6683408850288,
        "osmotic_coefficient": 0.926,
        "density": 1.03776
    },
    {
        "salt": "NH4Cl",
        "molality": 3.5,
        "molarity": 3.0753942934683045,
        "num_particles": 204.81665423449522,
        "osmotic_coefficient": 0.936,
        "density": 1.04319
    },
    {
        "salt": "NH4Cl",
        "molality": 4.0,
        "molarity": 3.4542704726005056,
        "num_particles": 230.04924035973394,
        "osmotic_coefficient": 0.945,
        "density": 1.04834
    },
    {
        "salt": "NH4Cl",
        "molality": 4.5,
        "molarity": 3.8199836464539043,
        "num_particles": 254.40519004632114,
        "osmotic_coefficient": 0.953,
        "density": 1.05322
    },
    {
        "salt": "NH4Cl",
        "molality": 5.0,
        "molarity": 4.173165911215783,
        "num_particles": 277.9265999537026,
        "osmotic_coefficient": 0.958,
        "density": 1.05786
    },
    {
        "salt": "NH4Cl",
        "molality": 5.5,
        "molarity": 4.514358478458322,
        "num_particles": 300.649513962067,
        "osmotic_coefficient": 0.963,
        "density": 1.06227
    },
    {
        "salt": "NH4Cl",
        "molality": 6.0,
        "molarity": 4.844073868273193,
        "num_particles": 322.6080651419696,
        "osmotic_coefficient": 0.969,
        "density": 1.06646
    },
    {
        "salt": "NH4NO3",
        "molality": 0.1,
        "molarity": 0.09923171954722812,
        "num_particles": 6.6086839124222,
        "osmotic_coefficient": 0.911,
        "density": 1.00026
    },
    {
        "salt": "NH4NO3",
        "molality": 0.2,
        "molarity": 0.1975199816222028,
        "num_particles": 13.15453497011423,
        "osmotic_coefficient": 0.89,
        "density": 1.00341
    },
    {
        "salt": "NH4NO3",
        "molality": 0.3,
        "molarity": 0.2948751915137007,
        "num_particles": 19.63824614972566,
        "osmotic_coefficient": 0.876,
        "density": 1.00652
    },
    {
        "salt": "NH4NO3",
        "molality": 0.4,
        "molarity": 0.39130355579345,
        "num_particles": 26.060230799638617,
        "osmotic_coefficient": 0.864,
        "density": 1.00958
    },
    {
        "salt": "NH4NO3",
        "molality": 0.5,
        "molarity": 0.48681685907454786,
        "num_particles": 32.421273757436744,
        "osmotic_coefficient": 0.855,
        "density": 1.0126
    },
    {
        "salt": "NH4NO3",
        "molality": 0.6,
        "molarity": 0.5814303426499615,
        "num_particles": 38.72239007040629,
        "osmotic_coefficient": 0.847,
        "density": 1.01559
    },
    {
        "salt": "NH4NO3",
        "molality": 0.7,
        "molarity": 0.6751493162931625,
        "num_particles": 44.96393336150856,
        "osmotic_coefficient": 0.84,
        "density": 1.01854
    },
    {
        "salt": "NH4NO3",
        "molality": 0.8,
        "molarity": 0.7679826892814744,
        "num_particles": 51.146496975270736,
        "osmotic_coefficient": 0.834,
        "density": 1.02145
    },
    {
        "salt": "NH4NO3",
        "molality": 0.9,
        "molarity": 0.8599391048103019,
        "num_particles": 57.27065653556275,
        "osmotic_coefficient": 0.829,
        "density": 1.02432
    },
    {
        "salt": "NH4NO3",
        "molality": 1.0,
        "molarity": 0.9510362087435407,
        "num_particles": 63.33758723049361,
        "osmotic_coefficient": 0.823,
        "density": 1.02716
    },
    {
        "salt": "NH4NO3",
        "molality": 1.2,
        "molarity": 1.130716838513807,
        "num_particles": 75.30404808348221,
        "osmotic_coefficient": 0.813,
        "density": 1.03277
    },
    {
        "salt": "NH4NO3",
        "molality": 1.4,
        "molarity": 1.3070155734374813,
        "num_particles": 87.04527980441348,
        "osmotic_coefficient": 0.803,
        "density": 1.0382
    },
    {
        "salt": "NH4NO3",
        "molality": 1.6,
        "molarity": 1.4800941219188053,
        "num_particles": 98.57205193083546,
        "osmotic_coefficient": 0.793,
        "density": 1.04353
    },
    {
        "salt": "NH4NO3",
        "molality": 1.8,
        "molarity": 1.6499880165450342,
        "num_particles": 109.88673087984573,
        "osmotic_coefficient": 0.785,
        "density": 1.04873
    },
    {
        "salt": "NH4NO3",
        "molality": 2.0,
        "molarity": 1.8168135810620938,
        "num_particles": 120.99706363871647,
        "osmotic_coefficient": 0.776,
        "density": 1.05383
    },
    {
        "salt": "NH4NO3",
        "molality": 2.5,
        "molarity": 2.2207802217717996,
        "num_particles": 147.90063692954175,
        "osmotic_coefficient": 0.758,
        "density": 1.06607
    },
    {
        "salt": "NH4NO3",
        "molality": 3.0,
        "molarity": 2.6070432995277106,
        "num_particles": 173.62517944050018,
        "osmotic_coefficient": 0.743,
        "density": 1.07769
    },
    {
        "salt": "NH4NO3",
        "molality": 3.5,
        "molarity": 2.9765914242114504,
        "num_particles": 198.23653110916575,
        "osmotic_coefficient": 0.728,
        "density": 1.08871
    },
    {
        "salt": "NH4NO3",
        "molality": 4.0,
        "molarity": 3.3305054189908594,
        "num_particles": 221.80667313987578,
        "osmotic_coefficient": 0.715,
        "density": 1.09921
    },
    {
        "salt": "NH4NO3",
        "molality": 4.5,
        "molarity": 3.669658030272898,
        "num_particles": 244.39372913630893,
        "osmotic_coefficient": 0.702,
        "density": 1.10921
    },
    {
        "salt": "NH4NO3",
        "molality": 5.0,
        "molarity": 3.9949936259788674,
        "num_particles": 266.06059258773837,
        "osmotic_coefficient": 0.69,
        "density": 1.11877
    },
    {
        "salt": "NH4NO3",
        "molality": 5.5,
        "molarity": 4.307320360232503,
        "num_particles": 286.8610853485133,
        "osmotic_coefficient": 0.679,
        "density": 1.12792
    },
    {
        "salt": "NH4NO3",
        "molality": 6.0,
        "molarity": 4.607440054368901,
        "num_particles": 306.84860751874345,
        "osmotic_coefficient": 0.67,
        "density": 1.1367
    },
    {
        "salt": "Na2HP",
        "molality": 0.1,
        "molarity": 0.09974328012505955,
        "num_particles": 6.642753080792652,
        "osmotic_coefficient": 0.918,
        "density": 1.0094
    },
    {
        "salt": "Na2HP",
        "molality": 0.2,
        "molarity": 0.19859452575986625,
        "num_particles": 13.226098000445317,
        "osmotic_coefficient": 0.878,
        "density": 1.0168
    },
    {
        "salt": "Na2HP",
        "molality": 0.3,
        "molarity": 0.29664264464852114,
        "num_particles": 19.755955881566887,
        "osmotic_coefficient": 0.865,
        "density": 1.0244
    },
    {
        "salt": "Na2HP",
        "molality": 0.4,
        "molarity": 0.3938579683814381,
        "num_particles": 26.230350852510334,
        "osmotic_coefficient": 0.845,
        "density": 1.0319
    },
    {
        "salt": "Na2HP",
        "molality": 0.5,
        "molarity": 0.4921744544759856,
        "num_particles": 32.77808158763763,
        "osmotic_coefficient": 0.834,
        "density": 1.0434
    },
    {
        "salt": "Na2HP",
        "molality": 1.0,
        "molarity": 0.9666244040072144,
        "num_particles": 64.37573769017305,
        "osmotic_coefficient": 0.783,
        "density": 1.0826
    },
    {
        "salt": "Na2HP",
        "molality": 1.5,
        "molarity": 1.4176631609278199,
        "num_particles": 94.414243425443,
        "osmotic_coefficient": 0.748,
        "density": 1.1152
    },
    {
        "salt": "Na2HP",
        "molality": 2.0,
        "molarity": 1.8532855898577376,
        "num_particles": 123.42604480402598,
        "osmotic_coefficient": 0.724,
        "density": 1.149
    },
    {
        "salt": "Na2HP",
        "molality": 2.5,
        "molarity": 2.294511327358745,
        "num_particles": 152.81101814192857,
        "osmotic_coefficient": 0.708,
        "density": 1.1931
    },
    {
        "salt": "Na2HP",
        "molality": 3.0,
        "molarity": 2.6721031810226923,
        "num_particles": 177.95807011438745,
        "osmotic_coefficient": 0.696,
        "density": 1.2113
    },
    {
        "salt": "Na2HP",
        "molality": 3.5,
        "molarity": 3.078179910277267,
        "num_particles": 205.00217214223238,
        "osmotic_coefficient": 0.688,
        "density": 1.2488
    },
    {
        "salt": "Na2HP",
        "molality": 4.0,
        "molarity": 3.4809989729174546,
        "num_particles": 231.8293184522407,
        "osmotic_coefficient": 0.689,
        "density": 1.2879
    }
]