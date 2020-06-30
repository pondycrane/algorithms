import collections
import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def convert_sorted_array_to_binary_search_tree(self, nums: typing.List[int]) -> TreeNode:
        if not nums: return None
        def dfs(l, r):
            if l > r: return None
            mid = (r - l) // 2 + l
            root = TreeNode(nums[mid])
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(nums) - 1)

"""
108. Convert Sorted Array to Binary Search Tree
Easy

2342

208

Add to List

Share
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
