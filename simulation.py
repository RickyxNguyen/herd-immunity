import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation():
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.next_person_id = 0
        self.total_dead = 0

        self.virus = Virus(virus_name, mortality_rate, basic_repro_num)
        file_name = (f'{virus_name}_simulation_pop_{population_size}_vp_'
                     f'{vacc_percentage}_infected_{initial_infected}.txt')
        self.logger = Logger(file_name)

        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        population = []
        infected_count = 0
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
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        return self.vacc_percentage==100 and self.total_dead == self.population_size

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        time_step_counter = 0

        while self._simulation_should_continue():
            (newly_infected_count, newly_dead_count) = self.time_step()
            self.logger.log_time_step(time_step_counter,
                                      newly_infected_count, newly_dead_count,
                                      self.total_infected, self.total_dead)
            time_step_counter += 1
            
        print(f'The simulation has ended after {time_step_counter} turns.')


    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        pass

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
