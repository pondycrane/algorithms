import collections
import random
import typing

import base.solution

class Solution(base.solution.Solution):
    def partition(self, start, end, pivot, nums) -> int:
        nums[start], nums[pivot] = nums[pivot], nums[start]
        pivot = i = start
        j = i + 1
        while j <= end:
            if nums[j] < nums[pivot]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        nums[pivot], nums[i] = nums[i], nums[pivot]
        return i

    def sort_an_array(self, nums: typing.List[int]) -> typing.List[int]:
        """
        Quicksort recursive
        """
        
        def quicksort_helper(nums, i, j):
            if i >= j:
                return
            
            pivot = random.randint(i, j)
            pivot = self.partition(i, j, pivot, nums)
            quicksort_helper(nums, i, pivot - 1)
            quicksort_helper(nums, pivot + 1, j)
        
        quicksort_helper(nums, 0, len(nums) - 1)
        return nums
    
    def sort_an_array(self, nums: typing.List[int]) -> typing.List[int]:
        """
        Quicksort iterative
        """
        queue = collections.deque()
        queue.append((0, len(nums) - 1))
        while queue:
            start, end = queue.pop()
            if start >= end:
                continue
            
            pivot = random.randint(start, end)
            pivot = self.partition(start, end, pivot, nums)
            queue.append((start, pivot - 1))
            queue.append((pivot + 1, end))
        
        return nums

"""
912. Sort an Array
Medium

Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""