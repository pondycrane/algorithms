from enum import Enum

import lib.ds_collections.linkedlist as linkedlist
import lib.ds_collections.treenode as treenode

class Verification(Enum):
    UNORDERED_SUBLISTS = 'UNORDERED_SUBLISTS'
    SUBSETS = 'SUBSETS' # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]] != [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3], []]
    UNORDERED_LIST = 'UNORDERED_LIST'
    EQUAL = 'EQUAL'
    TREE = 'TREE'
    TREE_STRICT = 'TREE_STRICT'
    LIST_OF_LINKEDLISTS = 'LIST_OF_LINKEDLISTS'
    LINKEDLIST = 'LINKEDLIST'
    DICTIONARY = 'DICTIONARY'

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
    elif enum_method == Verification.TREE_STRICT:
        return verify_tree_strict(output, answer)
    elif enum_method == Verification.LINKEDLIST:
        return verify_linkedlist(output, answer)
    elif enum_method == Verification.LIST_OF_LINKEDLISTS:
        return verify_list_of_linkedlists(output, answer)
    elif enum_method == Verification.DICTIONARY:
        return verify_dictionaries(output, answer)
    elif enum_method == Verification.SUBSETS:
        return verify_subsets(output, answer)
    else:
        raise Exception(f"{enum_method} not supported")

def verify_dictionaries(output, answer):
    if not output and not answer:
        return True
    
    if not isinstance(output, dict) or not isinstance(answer, dict):
        return False

    if len(output) != len(answer):
        return False
    
    for key in answer:
        if key not in output:
            return False
        
        if not isinstance(answer[key], dict):
            if output[key] != answer[key]:
                return False
        elif not verify_dictionaries(output[key], answer[key]):
            return False

    return True

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

def verify_tree_strict(output, answer):
    if not isinstance(answer, treenode.TreeNode):
        answer = treenode.TreeNode.deserialize(answer)
    def equals(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        return equals(t1.left, t2.left) and equals(t1.right, t2.right)
    return equals(output, answer)

def verify_unordered_list(output, answer):
    return sorted(output) == sorted(answer)

def verify_subsets(output, answer):
    if not output and not answer:
        return output == answer
    
    for data in [output, answer]:
        for l in data:
            l.sort()
        data.sort()
    return output == answer

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
