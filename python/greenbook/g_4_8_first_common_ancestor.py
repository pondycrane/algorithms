import typing

import base.solution
import lib.ds_collections.treenode as treenode


class Solution(base.solution.Solution):

    def g_4_8_first_common_ancestor(self, arr: typing.List[int], n1: int, n2: int) -> treenode.TreeNode:
        root = treenode.TreeNode.deserialize(arr)

        def first_common_ancestor(node, n1, n2):
            if not node:
                return None
            
            if node.val in [n1, n2]:
                return node.val
            
            left = first_common_ancestor(node.left, n1, n2)
            if isinstance(left, treenode.TreeNode):
                return left
            
            right = first_common_ancestor(node.right, n1, n2)
            if isinstance(right, treenode.TreeNode):
                return right
            
            if left is not None and right is not None:
                return node
            
            if isinstance(left, int):
                return left
            if isinstance(right, int):
                return right
            
            return None
        
        res = first_common_ancestor(root, n1, n2)
        return res if not isinstance(res, int) else None


