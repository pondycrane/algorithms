import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def equal_sum_subset_partition(self, s: List[int]) -> List[bool]:
        if len(s) < 2:
            return []

        target = sum(s) / 2
        if target % 1 != 0:
            return []

        res = [False] * len(s)
        if s[0] == target:
            res[0] = True
            return res

        dp = [set([s[0]])]
        found = False
        for i in range(1, len(s) - 1):
            dp.append(set([s[i]]))
            for num in dp[i - 1]:
                dp[i].add(num)
                dp[i].add(num + s[i])
            if target in dp[i]:
                found = True
                break
        
        if not found:
            return []

        # Restore bool list
        ind = len(dp) - 1
        while ind >= 0:
            if target in dp[ind] and (ind == 0 or target not in dp[ind - 1]):
                res[ind] = True
                target -= s[ind]
                if target == 0:
                    break

            ind -= 1
        return res
        


"""
Given a list of integers, return a list of booleans showing
a valid combination that can partition to equal sum (sum of True equals to
sum of False)
"""
