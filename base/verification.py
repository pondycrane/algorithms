from enum import Enum

import lib.ds_collections.linkedlist as linkedlist
import lib.ds_collections.treenode as treenode

class Verification(Enum):
    UNORDERED_SUBLISTS = 'UNORDERED_SUBLISTS'
    UNORDERED_LIST = 'UNORDERED_LIST'
    EQUAL = 'EQUAL'
    TREE = 'TREE'
    LIST_OF_LINKEDLISTS = 'LIST_OF_LINKEDLISTS'
    LINKEDLIST = 'LINKEDLIST'

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
    elif enum_method == Verification.LINKEDLIST:
        return verify_linkedlist(output, answer)
    elif enum_method == Verification.LIST_OF_LINKEDLISTS:
        return verify_list_of_linkedlists(output, answer)
    else:
        raise Exception(f"{enum_method} not supported")

def verify_list_of_linkedlists(output, answer):
    if len(output) != len(answer):
        return False
    
    for n1, n2 in zip(output, answer):
        if not verify_linkedlist(n1, n2):
            return False  
    return True

def verify_linkedlist(output, answer):
    if isinstance(output, list):
        output = linkedlist.ListNode.deserialize(output)
    if isinstance(answer, list):
        answer = linkedlist.ListNode.deserialize(answer)

    while output and answer:
        if output.val != answer.val:
            return False
        output = output.next
        answer = answer.next
    if output or answer:
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