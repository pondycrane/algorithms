import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def check_tree_has_sequence(self, root: typing.List[int], arr: typing.List[int]) -> int:
        root =  treenode.TreeNode.deserialize(root)
        
        def check(node, ind):
            if not node:
                return ind == len(arr)
            if ind >= len(arr) or node.val != arr[ind]:
                return False
            if ind == len(arr) - 1:
                return not node.left and not node.right
            return check(node.left, ind + 1) or check(node.right, ind + 1)

        return check(root, 0)