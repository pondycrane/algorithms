import typing

import base.solution
import lib.ds_collections.treenode as treenode


class Solution(base.solution.Solution):

    def g_4_9_bst_sequences(self, arr: typing.List[int]) -> typing.List[typing.List[int]]:
        root = treenode.TreeNode.deserialize(arr)

        def collect(root):
            if not root:
                return []
            
            if not root.left and not root.right:
                return [[root.val]]
            
            left = collect(root.left)
            right = collect(root.right)

            res = []
            for i in range(len(left)):
                for j in range(len(right)):
                    res.extend(interwove(left[i], right[j]))
            
            for arr in res:
                arr.append(root.val)

            return res

        def interwove(arr1, arr2):
            res = []
            def interwove_helper(ind1, ind2, curr):
                if ind1 == len(arr1) and ind2 == len(arr2):
                    res.append(curr)
                    return

                if ind1 == len(arr1):
                    res.append(curr + arr2[ind2:])
                    return
                if ind2 == len(arr2):
                    res.append(curr + arr1[ind1:])
                    return
                
                interwove_helper(ind1 + 1, ind2, curr + [arr1[ind1]])
                interwove_helper(ind1, ind2 + 1, curr + [arr2[ind2]])
            
            interwove_helper(0, 0, [])
            return res
        
        return [arr[::-1] for arr in collect(root)]

"""
4.9 BST Sequences: A binary search tree was created by traversing through an array from left
to right and inserting each element. Given a binary search tree with distinct elements, print 
all possible arrays that could have led to this tree.

EXAMPLE
Input: [2, 1, 3]
Output: [[2, 1, 3], [2, 3, 1]]
"""