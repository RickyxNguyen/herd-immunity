from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation
import os

class TestSimulation:
    def test_1(self):
        test_virus = Virus("Ebola", 0.8, 0.5)
        test_sim = Simulation(100, 0.5, test_virus.name, test_virus.mortality_rate, test_virus.repro_rate)

        test_sim.run()

        with open("Ebola_simulation_pop_100_vp_0.5_infected_1.txt", "rb") as f:
            first = f.readline()
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                f.seek(-2, os.SEEK_CUR)
            last = f.readline()

        assert last == b"Time step 2 ended, 0 are infected, 20 recently died, 50 got infected, 42 have died, beginning 3...\n"