import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def robbery(self, values: List[int]) -> int:
        dp = values.copy()
        for i in range(len(values)):
            for j in [2, 3]:
                if i - j >= 0:
                    dp[i] = max(dp[i - j] + values[i], dp[i])
        return max(dp[-2:])


"""
You can't rob two neighboring houses

Example One

Input: values = [6, 1, 2, 7]

Output: 13

Steal from the first and the last house.



Example Two

Input: values = [1, 2, 4, 5, 1]

Output: 7

Steal from the second and the fourth house.
"""
