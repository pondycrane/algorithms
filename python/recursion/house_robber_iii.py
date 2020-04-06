import typing

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):

    def house_robber_iii(self, arr: typing.List[int]) -> int:
        root = treenode.TreeNode.deserialize(arr)
        def build(root):
            if root is None:
                return 0, 0
            
            lrob, lskip = build(root.left)
            rrob, rskip = build(root.right)

            return (
                lskip + rskip + root.val,
                max(lrob, lskip) + max(rrob, rskip)
            )
        return max(build(root))


"""
337. House Robber III
Medium

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""