import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):

    def g_4_2_minimal_tree(self, arr: typing.List[int]) -> typing.List[int]:

        def build_tree(left, right):
            if left > right:
                return None
            
            mid = left + int((right - left) / 2)
            node = treenode.TreeNode(arr[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node
        
        return treenode.TreeNode.serialize(build_tree(0, len(arr) - 1))

            
"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique 
integer elements, write an algorithm to create a binary search 
tree with minimal height.
"""