import collections
import re
import collections
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def binary_tree_right_side_view(self, root: typing.List[int]) -> treenode.TreeNode:
        if not root: return []
        root = treenode.TreeNode.deserialize(root)
        result = []
        q = collections.deque([root])
        while q:
            l = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i == l - 1:
                    result.append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
        return result

"""
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
""" 
