import collections
import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def path_sum_ii(self, root: typing.List[int], sum: int) -> typing.List[typing.List[int]]:
        root = TreeNode.deserialize(root)
        res = []
        def dfs(root, slate, cur):
            if root is None: return
            if root.left is None and root.right is None:
                if cur + root.val == sum:
                    res.append(slate[:] + [root.val])
                    return
            slate.append(root.val)
            dfs(root.left, slate, cur + root.val)
            dfs(root.right, slate, cur + root.val)
            slate.pop()
        dfs(root, [], 0)
        return res

"""
113. Path Sum II
Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
