import collections
import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    """
    My solution
    """
    def binary_tree_level_order_traversal(self, root: typing.List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        if root is None: return []
        q = collections.deque([(0, root)])
        result = []
        while q:
            l, node = q.popleft()
            while len(result) <= l:
                result.append([])
            result[l].append(node.val)
            if node.left: q.append((l + 1, node.left))
            if node.right: q.append((l + 1, node.right))
        return result

    """
    Instructor solution
    """
    def binary_tree_level_order_traversal(self, root: typing.List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        if not root: return []
        q = collections.deque([root])
        result = []
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            result.append(temp)
        return result

"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
