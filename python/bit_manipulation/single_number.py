import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def single_number(self, arr: list) -> None:
        num = 0
        for n in arr:
            num ^= n
        
        return num ^ (0 ^ 0)


"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""