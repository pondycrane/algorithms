import collections
import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    """
    Recursive
    """
    def binary_tree_preorder_traversal(self, root: typing.List[int]) -> typing.List[int]:
        root = TreeNode.deserialize(root)
        res = []

        def preorder(n):
            if n is None: return
            res.append(n.val)
            preorder(n.left)
            preorder(n.right)

        preorder(root)
        return res

    """
    Generator
    """
    def binary_tree_preorder_traversal(self, root: typing.List[int]) -> typing.List[int]:
        root = TreeNode.deserialize(root)

        def preorder(n):
            if n is None: return
            yield n.val
            yield from preorder(n.left)
            yield from preorder(n.right)

        return list(preorder(root))

    """
    Iterative
    """
    def binary_tree_preorder_traversal(self, root: typing.List[int]) -> typing.List[int]:
        root = TreeNode.deserialize(root)

        if not root: return []
        def preorder(root):
            s = [root]
            while s:
                n = s.pop()
                yield n.val
                if n.right is not None:
                    s.append(n.right)
                if n.left is not None:
                    s.append(n.left)

        return list(preorder(root))


        
 
"""
144. Binary Tree Preorder Traversal
Medium

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
