import collections
import itertools
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def recover_binary_search_tree(self, root: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        
        """
        Record first, second everytime first >= second
        """
        first = second = prev = None
        def inorder(n):
            nonlocal first, second, prev
            if n is None: return
            inorder(n.left)
            
            # 'prev is None' means root node can be included to first
            if not first and (prev is None or prev.val >= n.val):
                first = prev
            
            if first and prev and prev.val >= n.val:
                second = n

            prev = n
            inorder(n.right)

        inorder(root)

        first.val, second.val = second.val, first.val
        
        return root
                
    

"""
99. Recover Binary Search Tree
Hard
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""
