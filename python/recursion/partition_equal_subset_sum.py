import collections
import typing

import base.solution

class Solution(base.solution.Solution):

    def partition_equal_subset_sum(self, nums: typing.List[int]) -> bool:
        counter = collections.Counter(nums)
        half = sum(nums) / 2
        if half % 1 != 0:
            return False
        
        def check(curr):
            if curr > half:
                return False
            if curr == half:
                return True
            
            for key in list(counter.keys()):
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
                if check(curr + key):
                    return True
                counter[key] += 1
                
            return False
        
        return check(0)

"""
416. Partition Equal Subset Sum
Medium

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""