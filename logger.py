class Logger(object):


    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        # This will open a 'w' file as data and write to it the pop_size, vacc_percentage, mortality_rate, repro_num 
        with self.open_file('w') as data:
            data.write(f'{pop_size}\t{vacc_percentage}\t{virus_name}\t'
                      f'{mortality_rate}\t{repro_rate}\n')

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        This will open a 'a' file as data and read through it to check if a person is infected of not infected 
        '''
        with self.open_file('a') as data:
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
        '''
        This will open a 'a' file as data and read through it to check if a person has died from an infection or not
        '''
        with self.open_file('a') as data:
            if did_die_from_infection:
                data.write(f'{person._id} died from infection \n')
            else:
                data.write(f'{person._id} survived infection \n')


    def log_time_step(self, time_step_number,newly_infected_count, newly_dead_people,
                    total_infected, total_dead):

        with self.open_file('a') as data:
            data.write(f'Time step {time_step_number} ended, '
                      f'{newly_infected_count} are infected, '
                      f'{newly_dead_people} recently died, '
                      f'{total_infected} got infected, '
                      f'{total_dead} have died, '
                      f'beginning {time_step_number + 1}...\n')
        '''
        This will allow me to open a file and access it
        '''

    def open_file(self, mode='r', buffering=-1, encoding=None, errors=None,
                    newline=None, closefd=True, opener=None):
            return open(f'{self.file_name}', mode, buffering, encoding, errors,
                        newline, closefd, opener)