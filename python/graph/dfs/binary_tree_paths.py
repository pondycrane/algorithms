import collections
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode


class Solution(base.solution.Solution):
    def binary_tree_paths(self, root: List[int]) -> List[str]:
        root = TreeNode.deserialize(root)

        def preorder(n, slate):
            if n is None:
                return
            slate.append(n.val)
            if n.left == n.right == None:
                res.append('->'.join(map(str, slate)))
            else:
                preorder(n.left, slate)
                preorder(n.right, slate)
            slate.pop()

        res = []
        preorder(root, [])
        return res



"""
257. Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
