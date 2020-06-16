import base.solution
import typing

import lib.ds_collections.linkedlist as linkedlist

class Solution(base.solution.Solution):
    def merge_k_sorted_lists(self, lists: typing.List[int]) -> linkedlist.ListNode:
        lists = [linkedlist.ListNode.deserialize(l) for l in lists]
        if not lists:
            return None
        
        def merge(l1, l2):
            n1, n2 = l1, l2
            r = linkedlist.ListNode(0)
            rn = r
            while n1 and n2:
                if n1.val < n2.val:
                    rn.next = n1
                    n1 = n1.next
                else:
                    rn.next = n2
                    n2 = n2.next
                rn = rn.next
            while n1:
                rn.next = n1
                n1 = n1.next
                rn = rn.next
            while n2:
                rn.next = n2
                n2 = n2.next
                rn = rn.next
            return r.next
        
        def divide_n_conquer(left, right):
            if left == right:
                return lists[left]
            elif left + 1 == right:
                return merge(lists[left], lists[right])
            else:
                mid = (right - left) // 2 + left
                return merge(
                    divide_n_conquer(left, mid),
                    divide_n_conquer(mid + 1, right)
                )
        
        return divide_n_conquer(0, len(lists) - 1)


"""
23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""