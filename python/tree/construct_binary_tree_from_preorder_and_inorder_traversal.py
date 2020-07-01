from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def construct_binary_tree_from_preorder_and_inorder_traversal(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inord_map = {v: i for i, v in enumerate(inorder)}
        
        def dfs(pl, pr, il, ir):
            if pl > pr: return None
            n = TreeNode(preorder[pl])
            if pl == pr: return n
            mid = inord_map[n.val]
            n.left = dfs(pl + 1, pl + (mid - il), il, mid - 1)
            n.right = dfs(pl + (mid - il) + 1, pr, mid + 1, il)
            return n

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
