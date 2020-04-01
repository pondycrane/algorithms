import typing

import base.solution
import lib.ds_collections.treenode as treenode

"""
Unfinished
"""

class RandomNode(treenode.TreeNode):
    def __init__(self, val):
        super().__init__(val)
        self.size = 1

    def find(self, val):
        node = self
        while node.val != val:


    def insert(self, val):
        node = self
        while node.val != val:
            if node.val > val:
                next_node = node.left
            else:
                next_node = node.right
            
            if next_node is None:
                break
            
            node = next_node
        
        if node.val == val:
            return
        
        if node.val > val:
            node.left = RandomNode(val)
        else:
            node.right = RandomNode(val)
        self.size += 1


class Solution(base.solution.Solution):

    def g_4_10_check_subtree(self, t1: typing.List[int], t2: typing.List[int]) -> bool:
