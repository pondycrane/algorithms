import json
import unittest

import base.testcases
import lib.path_utils


def test_generator(solution_obj, method_name, kwargs, answer, error):
    def test(self):
        positive_testcase = True
        try:
            output = getattr(solution_obj, method_name)(**kwargs)
        except Exception as e:
            assert type(e).__name__ == error, f"Error {e} is not expected {error}. Error msg: {e}"
            positive_testcase = False
        
        if positive_testcase:
            assert output == answer, f"output = {output} != {answer}"
    return test


class Solution:
    def __init__(self, problem):
        self.problem = problem
        self.method_name = problem[-1]

    def load_testcases(self):
        with open(
            lib.path_utils.generate_problem_paths(self.problem)['testcases']
        ) as sh:
            testcases = json.loads(sh.read())
        
        for testname, parameters in testcases.items():
            testcase_name = f"test_{testname}"
            kwargs = {k: v for k, v in parameters.items() if k not in ['answer', 'error']}
            setattr(
                base.testcases.TestCases,
                testcase_name,
                test_generator(
                    self,
                    self.method_name,
                    kwargs,
                    parameters.get('answer', None), parameters.get('error', None)
                )
            )
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(base.testcases.TestCases))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    def execute_testcases(self):
        # implement testcases
        pass
