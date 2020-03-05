import argparse
import os
import importlib
import json

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--problem', type=str)

def generate_problem_paths(problem):
    to_return = {}
    for folder, appendix in [
        ('python', '.py'),
        ('testcases', '.json')
    ]:
        to_return[folder] = "{}{}".format(
            os.path.join(
                os.path.dirname(
                    os.path.abspath(__file__)
                ),
                folder,
                *problem
            ),
            appendix
        )
    return to_return

def run_problem(problem):
    problem_paths = generate_problem_paths(problem)
    script_path, testcase_path = problem_paths['python'], problem_paths['testcases']

    with open(testcase_path) as sh:
        testcases = json.loads(sh.read())
    
    spec = importlib.util.spec_from_file_location(
        "module.name", f"{script_path}"
    )
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    solution_obj = solution.Solution(problem)
    
    for name, testcase in testcases.items():
        kwargs = {k: testcase[k] for k in testcase if k != 'answer'}
        output = getattr(solution_obj, problem[-1])(**kwargs)
        assert output == testcase['answer'], f"Testcase {name} output = {output} != {testcase['answer']}"

if __name__ == '__main__':
    args = parser.parse_args()
    problem = args.problem.split(',')
    run_problem(problem)