import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    Got timeout and wrong answer
    """
    def number_of_paths_in_a_matrix(self, matrix: List[List[int]]) -> int:
        dp = [row[:] for row in matrix]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if (i == 0 or j == 0) and dp[i][j] == 1:
                    if i == 0 and j == 0:
                        continue
                    dp[i][j] = (0 if i - 1 < 0 else dp[i - 1][j]) + \
                                (0 if j - 1 < 0 else dp[i][j - 1])
                elif dp[i][j] == 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1] % (10 ** 9 + 7)
                




"""
Find how many ways to reach bottom right corner by avoiding 0. You can only go right or down.
"""

