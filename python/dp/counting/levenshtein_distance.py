import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def levenshtein_distance(self, strWord1: str, strWord2: str) -> int:
        dp = [[0] * (len(strWord2) + 1) for _ in range(len(strWord1) + 1)]
        for i in range(len(strWord1) + 1):
            dp[i][0] = i
        for j in range(len(strWord2) + 1):
            dp[0][j] = j
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + int(not strWord1[i - 1] == strWord2[j - 1])
                )
        return dp[-1][-1]


"""
Example One

Input: cat, bat

Output: 1

Replace c with b.



Example Two

Input: qwe, q

Output: 2

1: Add w

2: Add e
"""
