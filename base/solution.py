import copy
import json
import unittest
import traceback
import sys

import base.testcases
import base.verification as verification
import lib.path_utils


def test_generator(solution_obj, method_name, kwargs, answer, error, verify_method):
    def test(self):
        input_data = copy.deepcopy(kwargs)
        try:
            output = getattr(solution_obj, method_name)(**kwargs)
            assert verification.verify(output, answer, verify_method)
        except Exception as e:
            if error is not None:
                assert type(e).__name__ == error, f"Error {e} is not expected {error}. Error msg: {e}"
            else:
                print("-"*60)
                traceback.print_exc(limit=3, file=sys.stdout)
                print("-"*60)

                if type(e).__name__ == 'AssertionError':
                    raise AssertionError(f"\nInput data: {input_data}\nOutput: {output} != {answer}")
                else:
                    raise e

    return test


class Solution:
    def __init__(self, problem):
        self.problem = problem
        self.method_name = problem[-1]

    def load_testsuite(self):
        with open(
            lib.path_utils.generate_problem_paths(self.problem)['testcases']
        ) as sh:
            json_data = json.loads(sh.read())
            testcases = json_data['testcases']
            verify_method = json_data['verify_method']
        for testname, testcase in testcases.items():
            testcase_name = f"test_{testname}"
            setattr(
                base.testcases.TestCases,
                testcase_name,
                test_generator(
                    self,
                    self.method_name,
                    testcase['parameters'],
                    testcase.get('answer', None),
                    testcase.get('error', None),
                    verify_method
                )
            )
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(base.testcases.TestCases))
        return suite

    def execute_testcases(self):
        # implement testcases
        pass
