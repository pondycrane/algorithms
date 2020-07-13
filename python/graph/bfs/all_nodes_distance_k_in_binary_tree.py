import collections
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode


class Solution(base.solution.Solution):
    def all_nodes_distance_k_in_binary_tree(self, root: List[List[int]], target: int, K: int) -> List[int]:
        root = TreeNode.deserialize(root)

        if not root: return []
        g = collections.defaultdict(list)
        def preorder(n, parent):
            if n is None:
                return

            g[n.val]
            if parent:
                g[parent.val].append(n.val)
                g[n.val].append(parent.val)
            preorder(n.left, n)
            preorder(n.right, n)

        preorder(root, None)
        
        # bfs
        q = collections.deque([target])
        visited = [True if i == target else False for i in range(len(g))]
        count = 0
        while q:
            print(q)
            if count == K: return list(q)
            l = len(q)
            for _ in range(l):
                v = q.popleft()
                for nv in g[v]:
                    if not visited[nv]:
                        visited[nv] = True
                        q.append(nv)
            count += 1
        return []
        

"""
863. All Nodes Distance K in Binary Tree
Medium

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
