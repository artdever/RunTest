import re


class Parser:
    test_results: list

    def parse_tests(self, text: str):
        # Regular expression pattern to match test results
        # \w Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
        # "?" Matches 0 or 1 (greedy) of the preceding RE.
        pattern = r"Running (\w+) \.\.\. Completed (\w+)(?: \[([\w\s:]+)\])?"

        self.test_results = re.findall(pattern, text)

    def result_to_dict(self):
        return [{'test_name': each[0], 'test_status': each[1], 'failure_type': each[2]} for each in self.test_results]
