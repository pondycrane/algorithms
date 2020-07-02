from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def inorder_successor_in_bst(self, root: List[int], p: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        p = TreeNode.deserialize(p)

        prev, successor = None, None
        def inorder(n):
            nonlocal prev, successor
            if n is None: return
            inorder(n.left)
            if prev is not None and prev.val == p.val:
                successor = n
            prev = n
            inorder(n.right)
        
        inorder(root)
        return successor

    """
    Iterative
    """    
    def inorder_successor_in_bst(self, root: List[int], p: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        p = TreeNode.deserialize(p)

        prev, s, t = None, [], root
        while s or t:
            while t:
                s.append(t)
                t = t.left
            
            t = s.pop()
            if prev and prev.val == p.val:
                return t
            
            prev = t
            t = t.right
        return None

    """
    Iterative with binary search
    """
    def inorder_successor_in_bst(self, root: List[int], p: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        p = TreeNode.deserialize(p)

        suc, t = None, root
        while t:
            if t.val <= p.val:
                t = t.right
            else:
                suc = t
                t = t.left
        return suc


"""
285. Inorder Successor in BST
Medium

Share
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""
