import typing

import base.solution
import lib.ds_collections.treenode as treenode


class Solution(base.solution.Solution):

    def g_4_5_valid_bst(self, arr: typing.List[int]) -> bool:
        root = treenode.TreeNode.deserialize(arr)

        def check(root, left, right):
            if not root:
                return True

            if left > root.val or right < root.val:
                return False
            
            if not check(root.right, root.val, right):
                return False
            
            if not check(root.left, left, root.val):
                return False
            
            return True
        
        return check(root, float('-inf'), float('inf'))

"""
4.5 Valid BST: Implement a function to check if a binary tree 
is a binary search tree.
"""