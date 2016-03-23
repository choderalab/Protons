from __future__ import print_function
from simtk import unit, openmm
from simtk.openmm import app
from constph.constph import MonteCarloTitration
from unittest import TestCase, skip
from . import get_data


class TestExplicit(TestCase):
    
    def setUp(self):
        self.temperature = 300.0 * unit.kelvin
        self.pressure = 1.0 * unit.atmospheres
        self.timestep = 1.0 * unit.femtoseconds
        self.collision_rate = 9.1 / unit.picoseconds
        self.pH = 9.6
        self.platform_name = 'CPU'
        testsystems = get_data('tyr_explicit', 'testsystems')
        self.positions = openmm.XmlSerializer.deserialize(open('{}/tyr.state.xml'.format(testsystems)).read()).getPositions(asNumpy=True)
        self.system = openmm.XmlSerializer.deserialize(open('{}/tyr.sys.xml'.format(testsystems)).read())
        self.prmtop = app.AmberPrmtopFile('{}/tyr.prmtop'.format(testsystems))
        self.cpin_filename = '{}/tyr.cpin'.format(testsystems)
        
    def test_tyrosine_instantaneous(self):
        """
        Test tyrosine in explicit solvent with an instanteneous state switch.
        """
        integrator = openmm.LangevinIntegrator(self.temperature, self.collision_rate, self.timestep)
        mc_titration = MonteCarloTitration(self.system, self.temperature, self.pH, self.prmtop, self.cpin_filename, integrator, debug=False,
                                           pressure=self.pressure, nsteps_per_trial=0, implicit=False)
        platform = openmm.Platform.getPlatformByName('CPU')
        context = openmm.Context(self.system, mc_titration.compound_integrator, platform)
        context.setPositions(self.positions)  # set to minimized positions
        integrator.step(10)  # MD
        mc_titration.update(context)  # protonation

    def test_tyrosine_ncmc(self):
        """
        Test tyrosine in explicit solvent with an ncmc state switch.
        """
        integrator = openmm.LangevinIntegrator(self.temperature, self.collision_rate, self.timestep)
        mc_titration = MonteCarloTitration(self.system, self.temperature, self.pH, self.prmtop, self.cpin_filename, integrator, debug=False,
                                           pressure=self.pressure, nsteps_per_trial=10, implicit=False)
        platform = openmm.Platform.getPlatformByName('CPU')
        context = openmm.Context(self.system, mc_titration.compound_integrator, platform)
        context.setPositions(self.positions)  # set to minimized positions
        integrator.step(10)  # MD
        mc_titration.update(context)  # protonation