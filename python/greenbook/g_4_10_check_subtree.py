import typing

import base.solution
import lib.ds_collections.treenode as treenode


class Solution(base.solution.Solution):

    def g_4_10_check_subtree(self, t1: typing.List[int], t2: typing.List[int]) -> bool:
        t1 = treenode.TreeNode.deserialize(t1)
        t2 = treenode.TreeNode.deserialize(t2)

        def check(t1, t2):
            if not t2:
                return True
            
            if not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            if not check(t1.left, t2.left):
                return False
            return check(t1.right, t2.right)
        
        def check_subtree(t1, t2):

            if check(t1, t2):
                return True
            
            if check(t1.left, t2):
                return True
            
            if check(t1.right, t2):
                return True
            
            return False
        
        return check_subtree(t1, t2)


"""
4.10 Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is
identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

T and S: O(n * m)
"""