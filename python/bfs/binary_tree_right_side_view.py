import collections
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def binary_tree_right_side_view(self, arr: typing.List[int]) -> typing.List[int]:
        root = treenode.TreeNode.deserialize(arr)
        res = []
        if not root:
            return res
        
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if level >= len(res):
                res.append(node.val)
            
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))
        return res






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