import typing

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def binary_tree_level_order_traversal(self, root: typing.List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        if root is None: return None
        sent = prev = TreeNode(0)

        def inorder(node):
            nonlocal prev
            if node is None: return
            inorder(node.left)
            # process node
            prev.right = node
            node.left = prev
            prev = node
            inorder(node.right)

        inorder(root)
        head = sent.right
        head.left = prev
        prev.right = head
        return head


        # 1. Perform inorder traversal and create the doubly linked list on the fly
        # 2. To access prev node after dfs, set prev as nonlocal variable
        """
        sentinal = TreeNode("fake")
        dfs (node):
            nonlocal prev
            if node is None: return
            if node.left is not null:
                dfs(node.left)
            prev.right = node
            node.left = prev
            prev = node
            if node.right is not null:
                dfs(node.right)
        
        # Root null check
        sent = new TreeNode("fake")
        prev = sent
        dfs(root)
        head = sent.right
        prev.right = head
        head.left = prev
        return head
        """


"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
Medium

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 
Example 1:

Input: root = [4,2,5,1,3]

Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]
"""
