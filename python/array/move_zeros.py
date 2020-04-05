import typing

import base.solution

class Solution(base.solution.Solution):
    def move_zeros(self, nums: typing.List[int]) -> typing.List[int]:
        p1 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p1] = nums[i]
                p1 += 1
            
        for i in range(p1, len(nums)):
            nums[i] = 0

        return nums



"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""