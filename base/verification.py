from enum import Enum

import lib.ds_collections.linkedlist as linkedlist
import lib.ds_collections.treenode as treenode

class Verification(Enum):
    UNORDERED_SUBLISTS = 'UNORDERED_SUBLISTS'
    UNORDERED_LIST = 'UNORDERED_LIST'
    EQUAL = 'EQUAL'
    TREE = 'TREE'
    LIST_OF_LINKEDLISTS = 'LIST_OF_LINKEDLISTS'

def verify(output, answer, verify_method):
    if not hasattr(Verification, verify_method):
        raise ValueError(f"{verify_method} not supported")

    enum_method = getattr(Verification, verify_method)
    if enum_method == Verification.UNORDERED_SUBLISTS:
        return verify_unordered_sublists(output, answer)
    elif enum_method == Verification.EQUAL:
        return output == answer
    elif enum_method == Verification.UNORDERED_LIST:
        return verify_unordered_list(output, answer)
    elif enum_method == Verification.TREE:
        return verify_tree(output, answer)
    elif enum_method == Verification.LIST_OF_LINKEDLISTS:
        return verify_list_of_linkedlists(output, answer)
    else:
        raise Exception(f"{enum_method} not supported")

def verify_list_of_linkedlists(output, answer):
    if len(output) != len(answer):
        return False
    
    for n1, n2 in zip(output, answer):
        if isinstance(n1, list):
            n1 = linkedlist.ListNode.deserialize(n1)
        if isinstance(n2, list):
            n2 = linkedlist.ListNode.deserialize(n2)

        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next
        if n1 or n2:
            return False
            
    return True

def verify_tree(output, answer):
    if output is None or isinstance(output, treenode.TreeNode):
        output = treenode.TreeNode.serialize(output)
    if output is None or isinstance(answer, treenode.TreeNode):
        answer = treenode.TreeNode.serialize(answer)
    return output == answer

def verify_unordered_list(output, answer):
    return sorted(output) == sorted(answer)

def verify_unordered_sublists(output, answer):
    if not output and not answer:
        return output == answer
    elif not output or not answer:
        return False

    for data in [output, answer]:
        if data:
            for i in range(len(data)):
                data[i].sort()
    if len(output) != len(answer):
        return False
    for i in range(len(output)):
        if output[i] != answer[i]:
            return False
    return True