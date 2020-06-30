from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def single_value_tree(self, root: List[int]) -> TreeNode:
        root = TreeNode.deserialize(root)
        
        c = 0
        def postord(t):
            nonlocal c
            if t is None: return set()
            total = postord(t.left) | postord(t.right) | set([t.val])
            if len(total) == 1:
                c += 1
            return total
        postord(root)
        return c

"""
Identify how many subtrees has only single value
"""
