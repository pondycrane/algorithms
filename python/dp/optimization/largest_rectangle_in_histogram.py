import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def largest_rectangle_in_histogram(self, heights: List[int]) -> int:
        """
        Bruteforce
        T: O(N2)
        S: O(1)
        """
        res = 0
        for i in range(len(heights)): # heights = [2, 1, 5, 6, 2, 3], i = 2
            mh = heights[i] # mh = 5
            res = max(res, heights[i]) # res = 6
            for j in range(i + 1, len(heights)): # j = 3
                mh = min(mh, heights[j]) # mh = 5
                res = max(res, mh * (j - i + 1)) # res = 10
        return res

    def largest_rectangle_in_histogram(self, heights: List[int]) -> int:
        """
        Divide and conquer
        T: O(NlogN) average case, O(N2) worst case (sorted)
        S: O(N) stack space
        """
        def dfs(l, r): # (0, 1) # (0, 0)
            if l > r:
                return 0
            if l == r:
                return heights[l]

            mid = l # mid = 0
            for i in range(l + 1, r + 1):
                if heights[i] < heights[mid]:
                    mid = i # mid = 1

            middle = heights[mid] * (r - l + 1)
            left = dfs(l, mid - 1) # 4
            right = dfs(mid + 1, r) # 4
            return max(middle, left, right)

        return dfs(0, len(heights) - 1)

    def largest_rectangle_in_histogram(self, heights: List[int]) -> int:
        """
        Stack, DP
        T: O(N)
        S: O(N)
        """
        stack = [-1]
        res = 0
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
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
