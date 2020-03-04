import argparse
import os
import importlib

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--problem', type=str)

def run_problem(problem):
    problem_path = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        'python',
        *problem
    )
    spec = importlib.util.spec_from_file_location(
        "module.name", f"{problem_path}.py"
    )
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

if __name__ == '__main__':
    args = parser.parse_args()
    problem = args.problem.split(',')
    run_problem(problem)