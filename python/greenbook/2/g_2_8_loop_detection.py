import typing

import base.solution
import lib.ds_collections.linkedlist as linkedlist

class Solution(base.solution.Solution):
    def g_2_8_loop_detection(self, arr: typing.List[int], pos: int) -> int:
        # Preparing data
        head = linkedlist.ListNode.deserialize(arr)
        if not head:
            return -1
        
        ind = 0
        curr = head
        loop_point = None
        while curr.next:
            if ind == pos:
                loop_point = curr
            curr = curr.next
            ind += 1
        curr.next = loop_point

        # Actual code
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if fast is None or fast.next is None:
            return -1
        
        p1 = head
        while p1 != slow:
            p1 = p1.next
            slow = slow.next

        return slow.val


"""
2.8 Loop Detection: Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists).
EXAMPLE
input: A -> B -> C -> D -> E -> C (the same C as earlier)
output: C
"""