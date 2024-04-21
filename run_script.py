import subprocess
from parser import Parser


class TestConfig:

    def __init__(self, count: int = 10, percentage: float = 0.3):
        self.count = count
        self.percentage = percentage

    def read_to_dict(self):
        parser = Parser()
        for i in range(self.count):
            # Run the .sh file and capture the output
            result_bytes = subprocess.check_output(['./runTest.sh'])
            # Decode the bytes to a string
            result_string = result_bytes.decode('utf-8')
            # Parse to list
            parser.parse_tests(result_string)
            # Create dictionary from list
            test_dict = parser.result_to_dict()
        return test_dict