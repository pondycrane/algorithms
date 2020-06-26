import typing

import base.solution

class Solution(base.solution.Solution):

    """
    Topdown recursion method.
    T: O(5**N)
    """
    def strobogrammatic_number_ii(self, n: int) -> typing.List[str]:
        side = [('1', '1'), ('6', '9'), ('9', '6'), ('8', '8'), ('0', '0')]
        middle = ['1', '8', '0']
        
        result = []
        def get_numbers(slate, pos):
            if pos == n // 2:
                if not (pos > 0 and slate.endswith('0')):
                    result.append(slate)
                return
            for l, r in side:
                get_numbers(l + slate + r, pos + 1)

        if n % 2 == 0:
            get_numbers('', 0)
        else:
            for c in middle:
                get_numbers(c, 0)

        return result

    """
    Bottom up iterative method.
    """
    def strobogrammatic_number_ii(self, n: int) -> typing.List[str]:
        result = [''] if n % 2 == 0 else ['1', '8', '0']
        pos = 0
        
        while pos < n // 2:
            side = [('1', '1'), ('6', '9'), ('9', '6'), ('8', '8')]
            side += [('0', '0')] * (pos != n // 2 - 1)
            size = len(result)
            result *= len(side)
            for i, (l, r) in enumerate(side):
                for j in range(i * size, i * size + size):
                    result[j] = l + result[j] + r
            pos += 1
        return result
 
"""
247. Strobogrammatic Number II
Medium

420

121

Add to List

Share
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
