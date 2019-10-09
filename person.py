import random

random.seed(42)


class Person(object):

    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    """
    Will see if person survives infection and then will set vaccinated to true and be cured if they survive
    """
    def did_survive_infection(self):
        if random.random() > self.infection.mortality_rate:
            self.is_vaccinated = True
            self.infection = None
            return True

        self.is_alive = False
        return False

