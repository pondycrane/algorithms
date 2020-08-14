import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def maximum_rectangle(self, matrix: List[List[str]]) -> int:
        """
        Stack, DP
        T: O(MN)
        S: O(MN)
        """
        if not matrix:
            return 0

        dp = [[0] * len(r) for r in matrix]
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 if i - 1 < 0 else dp[i - 1][j] + 1
        res = 0
        for heights in dp:
            stack = [-1]
            for i, h in enumerate(heights):
                while stack[-1] >= 0 and heights[stack[-1]] > h:
                    li = stack.pop()
                    res = max(res, heights[li] * (i - stack[-1] - 1))

                stack.append(i)

            while stack[-1] >= 0:
                li = stack.pop()
                w = len(heights) - stack[-1] - 1
                res = max(res, heights[li] * w)

        return res
        
 
"""
85. Maximal Rectangle
Hard

2971

71

Add to List

Share
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
