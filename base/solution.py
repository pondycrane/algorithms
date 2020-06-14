import copy
import functools
import json
import unittest
import traceback
import sys
import time

import base.testcases
import base.verification as verification
import lib.path_utils


count = 0

def benchmarking(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global count
        count += 1
        print(f'\n\n-Start---Running testcase {count!r}: {args!r}, {kwargs!r}')
        print(f'-Outputs-')
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f'-Done----{(end - start) * 1000!r} milisec, output: {output!r}\n')
        return output

    return wrapper


def test_generator(solution_obj, method_name, kwargs, answer, error, verify_method):
    def test(self):
        input_data = copy.deepcopy(kwargs)
        try:
            wrapped = benchmarking(
                getattr(solution_obj, method_name)
            )
            output = wrapped(**kwargs)
            assert verification.verify(output, answer, verify_method)
        except Exception as e:
            if error is not None:
                assert type(e).__name__ == error, f"Error {e} is not expected {error}. Error msg: {e}"
            else:
                if type(e).__name__ == 'AssertionError':
                    raise AssertionError(f"\nInput data: {str(input_data)}\nOutput: {output} != {answer}")
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
