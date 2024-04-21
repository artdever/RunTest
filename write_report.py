from result import TestRun
import socket
from datetime import datetime


class Report:

    def __init__(self, execution_time):
        self.execution_time = execution_time

    def write_in_log(self, test_run: TestRun):
        # Open a file in write mode
        with open('test_result.log', 'w') as file:
            # Write data
            file.write(f'DATE: {datetime.now().strftime("%m/%d/%Y")}\n')
            # Write hostname
            file.write(f'{socket.gethostname()}\n\n')
            # Write tests count
            file.write(f'{len(test_run.suit.values())} tests will be run:\n')
            # Write tests names
            for key in test_run.suit.keys():
                file.write(f'{key}\n')

            file.write('\n')  # Write new line
            # Ex. Running test1 ... Completed FAIL[Performance]
            for test in test_run.suit.values():
                file.write(f'Running {test.name} ... Completed {test.get_status()}')
                if test.get_status() == 'FAIL':
                    file.write(f'[{test.failure_type}]\n')
                else:
                    file.write('\n')

            file.write('-------------------------\n')
            # Filed count without unstable true and expected fail tests
            filed_count, name_and_type = self.__filed_count(test_run)
            file.write(f'FAILED - {filed_count}\n')

            for item in name_and_type:
                file.write(f'{item}\n')
            # Write execution time
            file.write(f'\nTOTAL RUNTIME: {self.execution_time}')


    def __filed_count(self, test_run: TestRun):
        count: int = 0
        name_type = []
        for test in test_run.suit.values():
            if test.is_expected():
                continue
            if test.get_status() == 'FAIL':
                name_type.append(f'{test.name} [{test.failure_type}]')
                count += 1
        return count, name_type
