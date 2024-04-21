from run_script import TestConfig
from time_stamp import measure_time
from result import TestRun
from write_report import Report


@measure_time
def run():
    obj = TestConfig(1, 0.3)
    test_dict = obj.read_to_dict()
    test_run = TestRun(test_dict)
    test_run.create_suit()
    return test_run


if __name__ == '__main__':
    result, execution_time = run()
    logger = Report(execution_time)
    logger.write_in_log(result)