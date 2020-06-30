from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def construct_binary_tree_from_inorder_and_postorder_traversal(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inord_map = {v: i for i, v in enumerate(inorder)}
        
        def dfs(pl, pr, il, ir):
            if pl > pr: return None
            node = TreeNode(postorder[pr])
            if pl == pr: return node
            inord_mid = inord_map[node.val]
            postord_mid = pr - (ir - inord_mid)
            node.left = dfs(pl, postord_mid - 1, il, inord_mid - 1)
            node.right = dfs(postord_mid, pr - 1, inord_mid + 1, ir)
            return node
        
        return dfs(0, len(postorder) - 1, 0, len(inorder) - 1)

"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
