import typing

import base.solution

class Solution(base.solution.Solution):
    def search_in_rotated_sorted_array(self, nums: typing.List[int], target: int) -> int:
        if not nums:
            return -1
        
        # 1. Binary search increment point
        def ident_rotate(left, right):
            if left > right:
                return 0
            
            mid = (right + left) // 2
            if mid == len(nums) - 1:
                return mid
            
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            
            if nums[left] > nums[mid]:
                return ident_rotate(left, mid)
            else:
                return ident_rotate(mid + 1, right)

        # 2. Binary search based on which side target is on
        # relative to the rotation index
        def binary_search(left, right):
            while left < right:
                mid = (right - left) // 2 + left
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        rotation = ident_rotate(0, len(nums))
        if nums[0] > target:
            return binary_search(rotation, len(nums))
        else:
            return binary_search(0, rotation)

"""
33. Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""