import base.solution
import math

class Solution(base.solution.Solution):
    def perfect_squares(self, n: int) -> int:
        memo = [float('inf')] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        srts = [i ** 2 for i in range(1, math.floor(n ** 0.5) + 1)]
        for i in range(1, len(memo)):
            if (i ** 0.5) % 1 == 0:
                memo[i] = 1
                continue

            memo[i] = min(
                memo[i],
                min([memo[i - num] + 1 for num in srts if num <= i])
            )
            
        return memo[n]

"""
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""