import collections
import random
import typing

import base.solution

class Solution(base.solution.Solution):
    def kth_largest_element_in_an_array(self, nums: typing.List[int], k: int) -> int:
        if len(nums) == 0 or k > len(nums) or k < 0:
            raise ValueError('Invalid input')
        
        queue = collections.deque()
        queue.append((0, len(nums) - 1))
        while queue:
            start, end = queue.pop()
            if start > end:
                continue
            
            pivot = random.randint(start, end)
            nums[start], nums[pivot] = nums[pivot], nums[start]
            pivot = i = start
            j = i + 1
            while j <= end:
                if nums[j] < nums[pivot]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            nums[pivot], nums[i] = nums[i], nums[pivot]

            if i == len(nums) - k:
                return nums[i]
            elif i < len(nums) - k:
                queue.append((i + 1, end))
            else:
                queue.append((start, i - 1))
        return -1
        

"""
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""