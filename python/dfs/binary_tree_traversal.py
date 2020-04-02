import collections

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def binary_tree_traversal(self, arr: list) -> None:
        root = treenode.TreeNode.deserialize(arr)

        res = []
        def dfs(node, index):
            if not node:
                return
            
            dfs(node.left, 2 * index + 1)
            res.append(node.val)
            dfs(node.right, 2 * index + 2)
        
        dfs(root, 0)
        return res

    def binary_tree_traversal(self, arr: list) -> None:
        root = treenode.TreeNode.deserialize(arr)
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            elif node.left:
                left = node.left
                node.left = None
                stack.append(node)
                stack.append(left)
            else:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
        return res
    
    """
    Morris Traversal
    T: O(N)
    S: O(1) # Not counting return array
    """
    def binary_tree_traversal(self, arr: list) -> None:
        root = treenode.TreeNode.deserialize(arr)
        res = []
        curr = root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                temp = curr
                nn = curr.left
                rm = curr.left
                while rm.right:
                    rm = rm.right
                rm.right = temp
                temp.left = None
                curr = nn
        return res




"""
94. Binary Tree Inorder Traversal
Medium

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""