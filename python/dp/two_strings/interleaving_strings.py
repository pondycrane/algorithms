import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def interleaving_strings(self, a: str, b: str, c: str) -> bool:
        if len(c) != len(a) + len(b):
            return False
        
        dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
        # dp[0][0] = True # Wrong, because the basecase will be overriden. But the result should be the same.
        for i in range(len(a) + 1):
            for j in range(len(b) + 1):
                dp[i][j] = (i == 0 and j == 0) or \
                            (i >= 1 and dp[i - 1][j] and a[i - 1] == c[i + j - 1]) or \
                            (j >= 1 and dp[i][j - 1] and b[j - 1] == c[i + j - 1])
        return dp[-1][-1]
        


"""
Interleaving Strings, all character of A % B, preserving order
A = xyzx
B = xyy

xyxyzxy -> valid
xyyxyxz -> invalid
xyxyzx -> invalid (too short)
xyyxyzx -> valid (B | A)
xyzxxyy ->  valid (A|B)

Given A, B, C, return True if C is a valid interleaving of A and B
A = 123
B = xyz
C = 1xy23z

Common suboptimal strategy: 2 points, however...
A = x......xy
B = x.......xz
C = x......xzx.....xy

This case leads to exponential time, since you have to try A and B over and over again, since they are mostly the same


#18
Two strings, DP table
A = xyzx
B = xyy
C = xyxyzxy
"""
