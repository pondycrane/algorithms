import base.solution
import typing

class Solution(base.solution.Solution):
    def maximum_subarray(self, nums: typing.List[int]) -> typing.List[int]:
        if not nums:
            return 0
        
        max_all = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_all = max(max_all, max_ending_here)
        
        return max_all



"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.




https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Kadane’s Algorithm:

Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far
"""