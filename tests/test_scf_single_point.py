
# test adapted from Quantum Espresso PWSCF v.5.3.0 (svn rev. 11974)
#  : PW/examples/example01

from __future__ import print_function

import numpy as np

from ase.build import bulk
from ase.units import Rydberg, Bohr
from espresso import Espresso


def test_al_scf_david(tmpdir):

    tmpdir.chdir()

    al = bulk('Al', 'fcc', 7.5 * Bohr)
    kpts = np.asarray([[0.0625000, 0.0625000, 0.0625000, 1.00],
                       [0.0625000, 0.0625000, 0.1875000, 3.00],
                       [0.0625000, 0.0625000, 0.3125000, 3.00],
                       [0.0625000, 0.0625000, 0.4375000, 3.00],
                       [0.0625000, 0.0625000, 0.5625000, 3.00],
                       [0.0625000, 0.0625000, 0.6875000, 3.00],
                       [0.0625000, 0.0625000, 0.8125000, 3.00],
                       [0.0625000, 0.0625000, 0.9375000, 3.00],
                       [0.0625000, 0.1875000, 0.1875000, 3.00],
                       [0.0625000, 0.1875000, 0.3125000, 6.00],
                       [0.0625000, 0.1875000, 0.4375000, 6.00],
                       [0.0625000, 0.1875000, 0.5625000, 6.00],
                       [0.0625000, 0.1875000, 0.6875000, 6.00],
                       [0.0625000, 0.1875000, 0.8125000, 6.00],
                       [0.0625000, 0.1875000, 0.9375000, 6.00],
                       [0.0625000, 0.3125000, 0.3125000, 3.00],
                       [0.0625000, 0.3125000, 0.4375000, 6.00],
                       [0.0625000, 0.3125000, 0.5625000, 6.00],
                       [0.0625000, 0.3125000, 0.6875000, 6.00],
                       [0.0625000, 0.3125000, 0.8125000, 6.00],
                       [0.0625000, 0.3125000, 0.9375000, 6.00],
                       [0.0625000, 0.4375000, 0.4375000, 3.00],
                       [0.0625000, 0.4375000, 0.5625000, 6.00],
                       [0.0625000, 0.4375000, 0.6875000, 6.00],
                       [0.0625000, 0.4375000, 0.8125000, 6.00],
                       [0.0625000, 0.4375000, 0.9375000, 6.00],
                       [0.0625000, 0.5625000, 0.5625000, 3.00],
                       [0.0625000, 0.5625000, 0.6875000, 6.00],
                       [0.0625000, 0.5625000, 0.8125000, 6.00],
                       [0.0625000, 0.6875000, 0.6875000, 3.00],
                       [0.0625000, 0.6875000, 0.8125000, 6.00],
                       [0.0625000, 0.8125000, 0.8125000, 3.00],
                       [0.1875000, 0.1875000, 0.1875000, 1.00],
                       [0.1875000, 0.1875000, 0.3125000, 3.00],
                       [0.1875000, 0.1875000, 0.4375000, 3.00],
                       [0.1875000, 0.1875000, 0.5625000, 3.00],
                       [0.1875000, 0.1875000, 0.6875000, 3.00],
                       [0.1875000, 0.1875000, 0.8125000, 3.00],
                       [0.1875000, 0.3125000, 0.3125000, 3.00],
                       [0.1875000, 0.3125000, 0.4375000, 6.00],
                       [0.1875000, 0.3125000, 0.5625000, 6.00],
                       [0.1875000, 0.3125000, 0.6875000, 6.00],
                       [0.1875000, 0.3125000, 0.8125000, 6.00],
                       [0.1875000, 0.4375000, 0.4375000, 3.00],
                       [0.1875000, 0.4375000, 0.5625000, 6.00],
                       [0.1875000, 0.4375000, 0.6875000, 6.00],
                       [0.1875000, 0.4375000, 0.8125000, 6.00],
                       [0.1875000, 0.5625000, 0.5625000, 3.00],
                       [0.1875000, 0.5625000, 0.6875000, 6.00],
                       [0.1875000, 0.6875000, 0.6875000, 3.00],
                       [0.3125000, 0.3125000, 0.3125000, 1.00],
                       [0.3125000, 0.3125000, 0.4375000, 3.00],
                       [0.3125000, 0.3125000, 0.5625000, 3.00],
                       [0.3125000, 0.3125000, 0.6875000, 3.00],
                       [0.3125000, 0.4375000, 0.4375000, 3.00],
                       [0.3125000, 0.4375000, 0.5625000, 6.00],
                       [0.3125000, 0.4375000, 0.6875000, 6.00],
                       [0.3125000, 0.5625000, 0.5625000, 3.00],
                       [0.4375000, 0.4375000, 0.4375000, 1.00],
                       [0.4375000, 0.4375000, 0.5625000, 3.00]])

    calc = Espresso(pw=15.0 * Rydberg, calculation='scf', kpts=kpts,
                    tprnfor=True, tstress=True, occupations='smearing',
                    smearing='marzari-vanderbilt', degauss=0.05,
                    outdir='al_scf')

    al.set_calculator(calc)

    calc.calculate(al)

    assert np.allclose(al.get_potential_energy(), -74.44991079398747)
    assert np.allclose(al.get_forces(), np.zeros(3))
    assert np.allclose(al.get_stress(), np.array([-0.02784864, -0.02784864,
                                                  -0.02784864, -0.0, -0.0, -0.0]))


def test_si_scf_cg(tmpdir):

    tmpdir.chdir()

    si = bulk('Si', 'fcc', 10.2 * Bohr)

    kpts = np.asarray([[0.1250000, 0.1250000, 0.1250000, 1.00],
                       [0.1250000, 0.1250000, 0.3750000, 3.00],
                       [0.1250000, 0.1250000, 0.6250000, 3.00],
                       [0.1250000, 0.1250000, 0.8750000, 3.00],
                       [0.1250000, 0.3750000, 0.3750000, 3.00],
                       [0.1250000, 0.3750000, 0.6250000, 6.00],
                       [0.1250000, 0.3750000, 0.8750000, 6.00],
                       [0.1250000, 0.6250000, 0.6250000, 3.00],
                       [0.3750000, 0.3750000, 0.3750000, 1.00],
                       [0.3750000, 0.3750000, 0.6250000, 3.00]])

    calc = Espresso(pw=18.0 * Rydberg, calculation='scf', kpts=kpts,
                    tprnfor=True, tstress=True, occupations='smearing',
                    smearing='marzari-vanderbilt', degauss=0.05,
                    convergence={'energy': 1e-6, 'mixing': 0.7,
                                 'maxsteps': 100, 'diag': 'cg'},
                    outdir='si_scf')

    si.set_calculator(calc)

    calc.calculate(si)

    assert np.allclose(si.get_potential_energy(), -152.90087195020132)
