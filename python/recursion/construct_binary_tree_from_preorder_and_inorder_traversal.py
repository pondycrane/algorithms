import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def construct_binary_tree_from_preorder_and_inorder_traversal(self, preorder: typing.List[int], inorder: typing.List[int]) -> treenode.TreeNode:
        ind_map = {val: key for key, val in enumerate(inorder)}
        curr_ind = 0
        def build_root(left, right):
            nonlocal curr_ind
            if left == right:
                return None
            
            val = preorder[curr_ind]
            index = ind_map[val]

            curr_ind += 1
            root = treenode.TreeNode(val)
            root.left = build_root(left, index)
            root.right = build_root(index + 1, right)
            return root
        
        return build_root(0, len(inorder))

