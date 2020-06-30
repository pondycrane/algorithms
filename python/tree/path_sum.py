import collections
import re
import collections
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def path_sum(self, root: typing.List[int], sum: int) -> bool:
        root = treenode.TreeNode.deserialize(root)
        def dfs(root, cur):
            if root is None: return False
            if root.left is None and root.right is None:
                return cur + root.val == sum
            if dfs(root.left, cur + root.val): return True
            return dfs(root.right, cur + root.val)
        return dfs(root, 0)


"""
112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
