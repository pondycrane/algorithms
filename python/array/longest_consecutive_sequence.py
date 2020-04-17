import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    """
    T: O(NlogN)
    S: O(1)
    """
    def longest_consecutive_sequence(self, nums: typing.List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        best = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1 :
                curr += 1
                if curr > best:
                    best = curr
            elif nums[i] == nums[i - 1]:
                continue
            else:
                curr = 1
        return best
    
    """
    Optimize time complexity
    T: O(N)
    S: O(N)
    """
    def longest_consecutive_sequence(self, nums: typing.List[int]) -> int:
        numset = set(nums)
        seen = set()
        best = 0
        for num in nums:
            if num - 1 not in numset:
                count = 0
                while num in numset:
                    seen.add(num)
                    count += 1
                    best = max(best, count)
                    num += 1

        return best

"""
128. Longest Consecutive Sequence
Hard

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""