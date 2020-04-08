import typing

import base.solution

class Solution(base.solution.Solution):
    def find_all_numbers_disappeared_in_array(self, nums: typing.List[int]) -> typing.List[int]:
        for num in nums:
            temp = num
            while nums[temp - 1] != -1 and temp != -1:
                temptemp = nums[temp - 1]
                nums[temp - 1] = -1
                temp = temptemp
        return [i + 1 for i in range(len(nums)) if nums[i] != -1]


"""
448. Find All Numbers Disappeared in an Array
Easy

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""