import typing

import base.solution

class Solution(base.solution.Solution):

    def valid_paranthesis(self, c: int) -> typing.List[str]:
        result = []

        def paranthesis(left, right, slate):
            # Backtracking
            if left < 0 or right < 0 or left > right:
                return
            
            # Basecase
            if left == right == 0:
                result.append(''.join(slate))
                return
            
            slate.append('(')
            paranthesis(left - 1, right, slate)
            slate[-1] = ')'
            paranthesis(left, right - 1, slate)
            slate.pop()

        paranthesis(c, c, [])
        return result

        # Divide and conquer: check leetcode

"""
Specifying the number of pairs we want, return the all
valid parenthesises.
Input: 3
Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
"""