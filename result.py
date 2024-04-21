class Test:

    def __init__(self, percentage: float = 0.3):
        self.percentage = percentage

    name: str
    failure_type: str
    expected_status: int = 0  # If it becomes greater than 0, then it is expected
    __status: bool = None
    fail_count = 0
    overall_count = 1

    def __calculate_dominant_status(self):
        # res = self.fail_count / self.overall_count
        if self.fail_count / self.overall_count > self.percentage:
            self.__status = False
        else:
            self.__status = True

    def get_status(self):
        self.__calculate_dominant_status()
        return 'PASS' if self.__status else 'FAIL'

    # The test is unstably true when it filed less than percentage.
    # When unstably will return False.
    def is_stably(self):
        return not (self.fail_count > 0 and self.__status == True)

    # Will return True if one time failure type was mentioned expected
    def is_expected(self):
        return self.expected_status > 0


class TestRun:
    # dict values should be TestCase type
    suit: dict = {}

    def __init__(self, test_list):
        self.test_list = test_list

    def __check_status(self, status):
        if status == "FAIL":
            return 1
        return 0

    def __check_fail_type(self, fail_type):
        if "Expected" in fail_type:
            return 1
        return 0

    def add_test_info(self, test):
        if test['test_name'] not in self.suit:
            case = Test()
            case.name = test['test_name']
            case.failure_type = test['failure_type']
            case.expected_status += self.__check_fail_type(test['failure_type'])
            case.__status = self.__check_status(test['test_status'])
            case.fail_count + self.__check_status(test['test_status'])
            self.suit.update({test['test_name']: case})

        else:

            self.suit[test['test_name']].overall_count += 1
            self.suit[test['test_name']].expected_status += self.__check_fail_type(test['failure_type'])
            self.suit[test['test_name']].fail_count += self.__check_status(test['test_status'])

    def create_suit(self):
        for each in self.test_list:
            self.add_test_info(each)
