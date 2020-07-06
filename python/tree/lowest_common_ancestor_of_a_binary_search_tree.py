from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def lowest_common_ancestor_of_a_binary_search_tree(self, root: List[int], p: int, q: int) -> TreeNode:
        root = TreeNode.deserialize(root)

        def find_node(node, num):
            if not node: return None
            if node.val == num: return node
            l = find_node(node.left, num)
            r = find_node(node.right, num)
            return l or r

        p = find_node(root, p)
        q = find_node(root, q)

        # Actual code starts from here
        def find_lca(root):
            if root in (None, p, q): return root
            l = find_lca(root.left)
            r = find_lca(root.right)
            if l and r: return root
            return l or r
        
        n = find_lca(root)
        return n.val

"""
235. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""
