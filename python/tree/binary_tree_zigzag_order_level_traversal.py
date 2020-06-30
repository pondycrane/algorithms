import collections
import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def binary_tree_zigzag_order_level_traversal(self, root: typing.List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        q = collections.deque([root])
        itor = 1
        result = []
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            if itor == 0: temp.reverse()
            result.append(temp)
            itor = 1 - itor
        return result


 
"""
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
