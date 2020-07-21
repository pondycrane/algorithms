import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def knights_tour(self, startdigit: int, phonenumberlength: int) -> int:
        if phonenumberlength == 0:
            return 0
        nm = {
            5: [],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        dp = [[0] * 10 for _ in range(phonenumberlength)]
        dp[0][startdigit] = 1
        for i in range(phonenumberlength - 1):
            for j in range(10):
                if dp[i][j] > 0:
                    for n in nm[j]:
                        dp[i + 1][n] += dp[i][j]
        return sum(dp[-1])


"""
Given a phone keypad
1 2 3
4 5 6
7 8 9
– 0 –

, a starting number and the length of the return digit, output how many
number can be returned using knights move.

Example One
Input: startdigit = 1, phonenumberlength = 2
Output: 2
Two possible numbers of length 2: 16, 18.


Example Two
Input: startdigit = 1, phonenumberlength = 3
Output: 5
The possible numbers of length 3: 160, 161, 167, 181, 183
"""
