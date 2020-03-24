import typing

import base.solution
import lib.ds_collections.treenode as treenode


class Solution(base.solution.Solution):

    def g_4_4_check_balanced(self, arr: typing.List[int]) -> bool:
        root = treenode.TreeNode.deserialize(arr)

        IMBALANCE = -1
        def check(root: treenode.TreeNode) -> int:
            if root is None:
                return 0
            
            left = check(root.left)
            if left == IMBALANCE:
                return left
            
            right = check(root.right)
            if right == IMBALANCE:
                return right
            
            if abs(left - right) > 1:
                return IMBALANCE
            
            return max(left, right) + 1
        
        return check(root) != IMBALANCE

"""
4.4 Check Balanced: Implement a function to check if a binary tree 
is balanced. For the purpose of the question, a balanced tree is defined 
to be a tree uch that the heights of the two subtres of any node never 
differ by more than one.
"""