import collections

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    """
    DFS in place
    T: O(N)
    S: O(1)
    """
    def flatten_binary_tree_to_linked_list(self, arr: list) -> None:
        root = treenode.TreeNode.deserialize(arr)
        if not root:
            return root
        
        def flatten(root):
            if not root:
                return None
            
            if not root.left and not root.right:
                return root
            
            left_tail = flatten(root.left)
            right_tail = flatten(root.right)

            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            return right_tail if right_tail else left_tail
        
        flatten(root)
        return root

    """
    DFS with queue
    T: O(N)
    S: O(N)
    """
    def flatten_binary_tree_to_linked_list_deque(self, arr: list) -> None:
        root = treenode.TreeNode.deserialize(arr)
        if not root:
            return root
        
        queue = collections.deque()
        def expand(root):
            if not root:
                return
            
            queue.append(root)
            expand(root.left)
            expand(root.right)
        
        expand(root)
        curr = root
        curr.left = None
        queue.popleft()
        while queue:
            curr.right = treenode.TreeNode(queue.popleft().val)
            curr.left = None
            curr = curr.right
        return root




"""
114. Flatten Binary Tree to Linked List
Medium

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""