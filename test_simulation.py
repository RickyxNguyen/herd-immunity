from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation
import os

ebola = Virus("Ebola", 0.8, 0.5)
hiv = Virus("HIV", 1.0, 0.4)
typhoid = Virus("Typhoid", 0.2, 0.3)
virus_list = [ebola, hiv, typhoid]

test_sim_1 = Simulation(1000, 0.6, virus_list[0].name, virus_list[0].mortality_rate, virus_list[0].repro_rate)
test_sim_2 = Simulation(1000, 0.1, virus_list[1].name, virus_list[1].mortality_rate, virus_list[1].repro_rate)
test_sim_3 = Simulation(1000, 0.9, virus_list[2].name, virus_list[2].mortality_rate, virus_list[2].repro_rate)

test_sim_1.run()
test_sim_2.run()
test_sim_3.run()

with open("Ebola_simulation_pop_1000_vp_0.6_infected_1.txt", "rb") as a:
    first_1 = a.readline()
    a.seek(-2, os.SEEK_END)
    while a.read(1) != b"\n":
        a.seek(-2, os.SEEK_CUR)
    last_1 = a.readline()

with open("HIV_simulation_pop_1000_vp_0.1_infected_1.txt", "rb") as b:
    first_2 = b.readline()
    b.seek(-2, os.SEEK_END)
    while b.read(1) != b"\n":
        b.seek(-2, os.SEEK_CUR)
    last_2 = b.readline()

with open("Typhoid_simulation_pop_1000_vp_0.9_infected_1.txt", "rb") as c:
    first_3 = c.readline()
    c.seek(-2, os.SEEK_END)
    while c.read(1) != b"\n":
        c.seek(-2, os.SEEK_CUR)
    last_3 = c.readline()

class TestSimulation:
    def test_1(self):
        assert last_1 == b"Time step 3 ended, 0 are infected, 115 recently died, 420 got infected, 331 have died, beginning 4...\n"
    
    def test_2(self):
        assert last_2 == b"Time step 3 ended, 0 are infected, 197 recently died, 900 got infected, 900 have died, beginning 4...\n"
    
    def test_3(self):
        assert last_3 == b"Time step 6 ended, 0 are infected, 0 recently died, 112 got infected, 26 have died, beginning 7...\n"