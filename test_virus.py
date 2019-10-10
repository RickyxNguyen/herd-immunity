import random
from virus import Virus


class TestVirus:
    def test_init(self):
        virus_name = "HIV"
        mortality_rate = 0.8
        repro_rate = 0.1
        virus = Virus(virus_name, mortality_rate, repro_rate)

        assert virus.name == virus_name
        assert virus.mortality_rate == mortality_rate
        assert virus.repro_rate ==  repro_rate

    def test_virus(self):
        virus_name = "Flu"
        mortality_rate = 0.8
        repro_rate = 0.4
        virus = Virus(virus_name, mortality_rate, repro_rate)

        assert virus.name == virus_name
        assert virus.mortality_rate == mortality_rate
        assert virus.repro_rate ==  repro_rate