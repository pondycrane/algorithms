from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    """
    Recursive
    """
    def upside_down(self, root: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        
        if not root: return None
        def upside_down(n):
            if n.left == n.right == None:
                return n
            new_root = upside_down(n.left)
            n.left.right = n
            n.left.left = n.right
            n.right = n.left = None
            return new_root
        
        return upside_down(root)
    
    """
    Iterative
    """        
    def upside_down(self, root: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)

        if not root: return None
        cur, s = root, [root]
        while cur.left is not None:
            cur = cur.left
            s.append(cur)

        new_root = cur = s.pop()
        while s:
            n = s.pop()
            cur.left = n.right
            cur.right = n
            n.left = n.right = None
            cur = n

        return new_root

"""
Turn a tree upside down. Each node of the input tree only has either 2 children or no children. Only left children have children.

Input:
       1
      / \
     2   3
    / \
   4   5
  / \
 6   7

Output:
       6
      / \
     7   4
        / \
       5   2
          / \
         3   1


Case2 Input:
  1
 / \
2   3

Output:
  2
 / \
3   1
"""
