class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = None

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # This will open a 'w' file as data and write to it the pop_size, vacc_percentage, mortality_rate, basic_repro_num 
        with self.open_file('w') as data:
            data.write(f'{pop_size}\t{vacc_percentage}\t{virus_name}\t'
                      f'{mortality_rate}\t{basic_repro_num}\n')

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        # This will open a 'x' file as data and read through it to check if a person is infected of not infected 
            with self.open_file('x') as data:
                if did_infect:
                    data.write(f'{person._id} infects {random_person._id}')
                else:
                    data.write(f'{person._id} didn\'t infect {random_person._id}')

                    if random_person_vacc:
                        data.write(' because vaccinated')
                    elif random_person_sick:
                        data.write(' because already sick')

            data.write('\n')

    def log_infection_survival(self, person, did_die_from_infection):

        # This will open a 'x' file as data and read through it to check if a person has died from an infection or not
        with self.open_file('x') as data:
            if did_die_from_infection:
                data.write(f'{person._id} died from infection\n')
            else:
                data.write(f'{person._id} survived infection\n')
            data.write('/n')

    def log_time_step(self, time_step_number,newly_infected_count, newly_dead_count,
                    total_infected, total_dead):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        with self.open_file('x') as data:
            data.write(f'Time step {time_step_number} ended, '
                      f'{newly_infected_count} are infected, '
                      f'{newly_dead_count} recently died, '
                      f'{total_infected} got infected, '
                      f'{total_dead} have died, '
                      f'beginning {time_step_number + 1}...\n')
