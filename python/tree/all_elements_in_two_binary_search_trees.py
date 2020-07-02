import collections
import itertools
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def all_elements_in_two_binary_search_trees(self, root1: List[int], root2: List[int]) -> List[int]:
        root1 = TreeNode.deserialize(root1)
        root2 = TreeNode.deserialize(root2)
        
        def inorder(n):
            if n is None: return
            yield from inorder(n.left)
            yield n.val
            yield from inorder(n.right)

        def consume(g):
            try:
                return next(g)
            except StopIteration as e:
                return None

        def merge_values(root1, root2):
            g1, g2 = inorder(root1), inorder(root2)
            n1, n2 = consume(g1), consume(g2)
            while n1 is not None and n2 is not None:
                if n1 < n2:
                    yield n1
                    n1 = consume(g1)
                else:
                    yield n2
                    n2 = consume(g2)
            while n1 is not None:
                yield n1
                n1 = consume(g1)
            while n2 is not None:
                yield n2
                n2 = consume(g2)
        
        return list(merge_values(root1, root2))
            

"""
1305. All Elements in Two Binary Search Trees
Medium

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""
