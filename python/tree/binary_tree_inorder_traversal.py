import collections
import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    """
    Iterative
    """
    def binary_tree_inorder_traversal(self, root: typing.List[int]) -> typing.List[int]:
        root = TreeNode.deserialize(root)
        s, t, res = [], root, []
        while s or t:
            while t:
                s.append(t)
                t = t.left
            t = s.pop()
            res.append(t.val)
            t = t.right
        return res

    """
    Recursive
    """
    def binary_tree_inorder_traversal(self, root: typing.List[int]) -> typing.List[int]:
        root = TreeNode.deserialize(root)
        res = []

        def inorder(n):
            if n is None: return
            inorder(n.left)
            res.append(n.val)
            inorder(n.right)

        inorder(root)
        return res

    """
    Recursive generator
    """
    def binary_tree_inorder_traversal(self, root: typing.List[int]) -> typing.List[int]:
        root = TreeNode.deserialize(root)
        def inorder(n):
            if n is None: return
            yield from inorder(n.left)
            yield n.val
            yield from inorder(n.right)

        return list(inorder(root))
        
 
"""
94. Binary Tree Inorder Traversal
Medium

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
