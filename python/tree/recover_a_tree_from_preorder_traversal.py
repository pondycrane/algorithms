import collections
import re
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def recover_a_tree_from_preorder_traversal(self, S: str) -> treenode.TreeNode:
        if not S: return None
        q = collections.deque()
        parent = []
        for l, n in re.findall(r'(-*)([0-9]+)', S):
            q.append((len(l), treenode.TreeNode(int(n))))
        level, root = q.popleft()
        node = root
        while q:
            if q[0][0] > level:
                nl, nn = q.popleft()
                if not node.left:
                    node.left = nn
                else:
                    node.right = nn
                parent.append((level, node))
                level, node = nl, nn
            else:
                level, node = parent.pop()
        return root
    

"""
1028. Recover a Tree From Preorder Traversal

Share
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

 

Example 1:



Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:



Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
 

Example 3:



Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Note:

The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
"""