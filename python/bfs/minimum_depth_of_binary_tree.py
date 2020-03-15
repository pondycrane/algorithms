import collections
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def minimum_depth_of_binary_tree(self, arr: typing.List[int]) -> int:
        root = treenode.TreeNode.deserialize(arr)
        if not root:
            return 0

        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return -1







"""
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""