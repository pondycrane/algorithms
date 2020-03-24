import typing

import base.solution
import lib.ds_collections.treenode as treenode
import lib.ds_collections.linkedlist as linkedlist


class Solution(base.solution.Solution):

    def g_4_3_list_of_depths(self, arr: typing.List[int]) -> typing.List[linkedlist.ListNode]:
        root = treenode.TreeNode.deserialize(arr)

        res = []
        tails = {}
        def process(root, depth):
            
            if not root:
                return

            node = linkedlist.ListNode(root.val)
            if depth >= len(res):
                res.append(node)
                tails[depth] = node
            else:
                tails[depth].next = node
                tails[depth] = node
            process(root.left, depth + 1)
            process(root.right, depth + 1)
        
        process(root, 0)
        return res

"""
4.3 List of Depths: Given a binary tree, design an algorithm which 
creates a linked list of all the nodes at each depth (e.g., if you 
have a tree with depth D, you'll have D linked lists).
"""