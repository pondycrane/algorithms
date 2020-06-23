import typing

import base.solution

class Solution(base.solution.Solution):

    """
    Recursive approach.
    """
    def generate_all_subsets_of_a_set(self, s: str) -> typing.List[str]:
        result = []
        def recursion(slate, pos):
            if pos == len(s):
                result.append(''.join(slate))
                return
            slate.append(s[pos])
            recursion(slate, pos + 1)
            slate.pop()
            recursion(slate, pos + 1)
        recursion([], 0)
        return result
    
    """
    Iterative approach.
    """
    def generate_all_subsets_of_a_set(self, s: str) -> typing.List[str]:
        result = [""]
        for i in range(len(s)):
            for j in range(0, len(result)):
                result.append(result[j] + s[i])
        return result