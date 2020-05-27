import base.solution
"""
There are one original file and one to override. Return
the updated json.
"""

class Solution(base.solution.Solution):

    def override_json_file(self, original: dict, override: dict) -> int:
        if original == override:
            return original
        
        if not original:
            return override

        def update(original, override):
            for key in override:
                if key not in original or not isinstance(override[key], dict):
                    original[key] = override[key]
                else :
                    update(original[key], override[key])
        
        update(original, override)
        return original
        
        