import collections
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def second_minimum_node_in_a_binary_tree(self, root: List[int]) -> int:
        root = TreeNode.deserialize(root)
        
        # Root has to be min1, since node value has to be the smaller node.
        # So root value will be the leftest node value
        def pre_order(t):
            nonlocal min2
            # base
            if t is None: return

            # rec
            # current
            if min1 < t.val < min2:
                min2 = t.val

            # left/right if current is same as min1
            # keep looking for min2
            if min1 == t.val:
                pre_order(t.left)
                pre_order(t.right)

        min1, min2 = root.val, float("inf")
        pre_order(root)
        return min2 if min2 < float("inf") else -1

"""
671. Second Minimum Node In a Binary Tree
Easy

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
