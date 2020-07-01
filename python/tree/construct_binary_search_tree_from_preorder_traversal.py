from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def construct_binary_search_tree_from_preorder_traversal(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder[:])
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
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""
