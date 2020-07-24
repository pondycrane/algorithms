import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    I only observed the recursive relation, but didn't see the 'not cut' route, leading to hardcoding 0-6
    T(N2)
    S(N)
    """
    def cut_the_rope(self, n: int) -> int:
        dic = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 4,
            5: 6,
            6: 9
        }
        if n <= 6:
            return dic[n]
        
        dp = [0] * (n + 1)
        for num in dic:
            dp[num] = dic[num]
        
        for i in range(7, len(dp)):
            m = float('-inf')
            j = 1
            while i - j >= 0 and j * dp[i - j] > m:
                m = j * dp[i - j]
                j += 1
            dp[i] = m
        return dp[n]

    """
    Consider uncut
    f(n) = Max  (i * (n - i), f(n - 1) * i)
           0<i<n
                   Uncut         Cut

    T(N2)
    S(N)
    """
    def cut_the_rope(self, n: int) -> int:
        if n < 2: return 0
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(
                    dp[i],
                    max(
                        j * (i - j), dp[j] * (i - j)
                    )
                )
        return dp[n]
        
 
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
