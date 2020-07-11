import collections
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def largest_bst_subtree(self, root: List[int]) -> int:
        root = TreeNode.deserialize(root)
        if root is None: return 0
        
        def postorder(n):
            if n.left == n.right == None:
                return 1, n.val, n.val

            if n.left is None:
                lc, lmin, lmax = 0, n.val, float('-inf')
            else:
                lc, lmin, lmax = postorder(n.left)

            if n.right is None:
                rc, rmin, rmax = 0, float('inf'), n.val
            else:
                rc, rmin, rmax = postorder(n.right)
            
            if n.val <= lmax or n.val >= rmin:
                return max(rc, lc), float('-inf'), float('inf')

            return rc + lc + 1, lmin, rmax

        c, _, _ = postorder(root)
        return c

            

"""
333. Largest BST Subtree
Medium

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""
