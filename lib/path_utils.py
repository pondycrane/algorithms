import importlib.util
import os

def generate_problem_paths(problem):
    to_return = {}
    for folder, appendix in [
        ('python', '.py'),
        ('testcases', '.json')
    ]:
        to_return[folder] = "{}{}".format(
            os.path.join(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                ),
                folder,
                *problem
            ),
            appendix
        )
    return to_return

def load_solution(problem):
    spec = importlib.util.spec_from_file_location(
        "module.name", f"{generate_problem_paths(problem)['python']}"
    )
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution.Solution(problem)