import collections
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def diameter_of_binary_tree(self, root: typing.List[int]) -> bool:
        root = treenode.TreeNode.deserialize(root)
        if not root: return 0
        best = 0
        def dfs(root):
            nonlocal best
            if root is None: return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            best = max(lh + rh, best)
            return max(lh, rh) + 1
        dfs(root)
        return best


"""
543. Diameter of Binary Tree
Easy

Share
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
