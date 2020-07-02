from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def insert_into_a_binary_search_tree(self, root: List[int], val: int) -> TreeNode:
        root = TreeNode.deserialize(root)
        new_node = TreeNode(val)
        if root is None: return new_node
        prev = None
        cur = root
        while cur is not None:
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if prev.val > val:
            prev.left = new_node
        else:
            prev.right = new_node
        return root
    
    """
    Recursive
    """
    def insert_into_a_binary_search_tree(self, root: List[int], val: int) -> TreeNode:
        root = TreeNode.deserialize(root)
        
        def inorder(n):
            if n is None: return TreeNode(val)
            if val < n.val:
                n.left = inorder(n.left)
            else:
                n.right = inorder(n.right)
            return n

        return inorder(root)

    

"""
701. Insert into a Binary Search Tree
Medium

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
 

Constraints:

The number of nodes in the given tree will be between 0 and 10^4.
Each node will have a unique integer value from 0 to -10^8, inclusive.
-10^8 <= val <= 10^8
It's guaranteed that val does not exist in the original BST.
"""
