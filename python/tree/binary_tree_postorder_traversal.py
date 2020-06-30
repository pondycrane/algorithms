from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def binary_tree_postorder_traversal(self, root: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        
        if not root: return []
        s, s1 = [root], []
        while s:
            n = s.pop()
            s1.append(n)
            if n.left is not None:
                s.append(n.left)
            if n.right is not None:
                s.append(n.right)
        
        return [n.val for n in reversed(s1)]

"""
145. Binary Tree Postorder Traversal
Hard

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

