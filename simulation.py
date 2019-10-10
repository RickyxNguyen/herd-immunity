import random
import sys
from person import Person
from logger import Logger
from virus import Virus

random.seed(42)

class Simulation():
    ''' 
    Initializes and will create a file for simulation
    '''
    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, repro_rate, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.next_person_id = 0
        self.total_dead = 0

        self.virus = Virus(virus_name, mortality_rate, repro_rate)
        file_name = (f'{virus_name}_simulation_pop_{population_size}_vp_'
                     f'{vacc_percentage}_infected_{initial_infected}.txt')
        self.logger = Logger(file_name)

        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):

        population = []
        infected_count = 0

        """
        This will build population by creating people until you have enoguh infected people with the virus
        and then it will randomly add normal or vaccinated people into the array until length of array condition is met
        """

        while len(population) != self.population_size:
            if infected_count != initial_infected:
                population.append(Person(self.next_person_id,
                                         is_vaccinated=False,
                                         infection=self.virus))
                infected_count += 1
            else:
                is_vaccinated = random.random() < self.vacc_percentage
                population.append(Person(self.next_person_id, is_vaccinated))

            self.next_person_id += 1

        return population

    def _simulation_should_continue(self):
        """
        This will check if either everyone alive is vaccinated or if everyone is dead and will
        end the game if either condition happens
        """
        return (self.current_infected > 0 and
                self.total_dead < self.population_size)
    def run(self):
        """
        This will check if the simulation has ended in the beginning and record the infected and dead people
        and will then run the simulation and increment each step by one
        """
        time_step_counter = 0

        while self._simulation_should_continue():
            (newly_infected_people, newly_dead_people) = self.time_step()
            self.logger.log_time_step(time_step_counter,
                                      newly_infected_people, newly_dead_people,
                                      self.total_infected, self.total_dead)
            time_step_counter += 1
            
        print(f'The simulation has ended after {time_step_counter} turns.')


    def time_step(self):

        """
        Lambda function will create a list of people that are alive in the population array
        """

        alive = list(filter(lambda p: p.is_alive, self.population))

        """
        Lambda function will create a list of infected people that are currently alive 
        """

        infected = list(filter(lambda p: p.infection, alive))

        """
        This will loop through infected people and run different scenarios to see if the random_person
        will be infected or not randomly from the list of 100 interactions
        """

        for person in infected:
            for _ in range(100):
                self.interaction(person, random_person=random.choice(alive))

        newly_dead_people = 0

        """
        This will loop through the infected people array and see if the random_person survived or not
        and if they did it will increment the newly_dead_people
        """

        for person in infected:
            if person.did_survive_infection():
                self.logger.log_infection_survival(person, did_die_from_infection=False)
            else:
                self.logger.log_infection_survival(person, did_die_from_infection=True)
                newly_dead_people += 1

        self.total_dead += newly_dead_people
        newly_infected_people = len(self.newly_infected)

        """
        This will log the amount of newly_infected and will then call on _infect_newly_infected to update all the 
        infected's stats
        """

        self._infect_newly_infected()

        return (newly_infected_people, newly_dead_people)

    def interaction(self, person, random_person):

        assert person.is_alive == True
        assert random_person.is_alive == True

        """
        This will check to see if person is vaccinated and if not, then will see if they are already sick and if not,
        will randomly check to see if the person is lucky enough to not get infected
        """

        if random_person.is_vaccinated:

            self.logger.log_interaction(person, random_person,
                                        did_infect=False, random_person_vacc=True)
        elif (random_person.infection != None or
              random_person._id in self.newly_infected):

            self.logger.log_interaction(person, random_person,
                                        did_infect=False, random_person_sick=True)
        else:
            if random.random() <= person.infection.repro_rate:
                self.newly_infected.append(random_person._id)

                self.logger.log_interaction(person, random_person,
                                            did_infect=True)
            else:
                self.logger.log_interaction(person, random_person,
                                            did_infect=False)

    def _infect_newly_infected(self):
        ''' 
        This will create an array of people that is newly infected in the population by checking if they are infected
        '''
        infected_people = list(filter(lambda p: p._id in self.newly_infected,
                                      self.population))
        '''
        This will iterate through all the people that got infected and assign them the virus
        '''
        for person in infected_people:
            person.infection = self.virus

        self.current_infected = len(self.newly_infected)
        self.total_infected += self.current_infected
        self.newly_infected.clear()


if __name__ == "__main__":
    params = sys.argv[1:]

    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    repro_rate = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    simulation = Simulation(pop_size, vacc_percentage, virus_name,
                            mortality_rate, repro_rate, initial_infected)
    simulation.run()
