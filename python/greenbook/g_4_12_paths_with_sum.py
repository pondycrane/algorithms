import typing
import collections

import base.solution
import itertools
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):

    def g_4_12_paths_with_sum(self, arr: typing.List[int], target: int) -> int:
        root = treenode.TreeNode.deserialize(arr)

        trace = collections.defaultdict(int)
        trace[0] = 1

        def collect_sum_hits(node, curr):
            if not node:
                return 0
            
            curr += node.val
            prev = curr - target
            sum_hits = trace[prev]

            trace[curr] += 1
            sum_hits += collect_sum_hits(node.left, curr)
            sum_hits += collect_sum_hits(node.right, curr)
            trace[curr] -= 1

            return sum_hits
        
        return collect_sum_hits(root, 0)



"""
4.12 Paths with Sum: You are given a binarytree inwhich each node contains an integer value 
(which might be positive or negative). Design an algorithm to count the number of paths that
sum to a given vlaue. The path does not need to start or end at the root or a leaf, but it
must go downwards (traveling only from parent nodes to child nodes).
"""
