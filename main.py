import argparse
import datetime

import lib.path_utils

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--problem', type=str)

def run_problem(problem):
    solution_obj = lib.path_utils.load_solution(problem)
    solution_obj.load_testcases()

if __name__ == '__main__':
    args = parser.parse_args()
    problem = args.problem.split(',')
    run_problem(problem)