from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode

class Solution(base.solution.Solution):
    def merge_two_bsts(self, root1: List[int], root2: List[int]) -> TreeNode:
        root1 = TreeNode.deserialize(root1)
        root2 = TreeNode.deserialize(root2)
        
        a1, a2 = [], []
        def inorder(n, a):
            if n is None: return
            inorder(n.left, a)
            a.append(n)
            inorder(n.right, a)

        def merge(a1, a2):
            a = []
            l1, l2 = 0, 0
            while l1 < len(a1) and l2 < len(a2):
                if a1[l1].val < a2[l2].val:
                    a.append(a1[l1])
                    l1 += 1
                else:
                    a.append(a2[l2])
                    l2 += 1
            while l1 < len(a1):
                a.append(a1[l1])
                l1 += 1
            while l2 < len(a2):
                a.append(a2[l2])
                l2 += 1
            return a

        def bst(l, r, a):
            if l > r: return None
            mid = (r - l) // 2 + l
            n = a[mid]
            n.left = bst(l, mid - 1, a)
            n.right = bst(mid + 1, r, a)
            return n
            
        inorder(root1, a1)
        inorder(root2, a2)
        return bst(0, len(a1) + len(a2) - 1, merge(a1, a2))

"""
Merge two trees into a balanced tree, with node number the sum of the two node counts.
"""
