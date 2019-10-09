import random
from person import Person
from virus import Virus


class TestPerson:
    def test_init(self):
        ebola = Virus("Ebola", 0.8, 0.1)
        person = Person(0, False, ebola)

        assert person.infection == ebola
        assert person.is_alive == True
        assert person.is_vaccinated == False
        assert person._id == 0

    def test_did_survive_infection(self):
        ebola = Virus("Ebola", 0.8, 0.1)
        person = Person(0, False, ebola)

        if person.did_survive_infection():
            assert person.is_alive == True
            assert person.is_vaccinated == True
            assert person.infection == None
        else:
            assert person.is_alive == False