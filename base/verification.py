from enum import Enum

class Verification(Enum):
    UNORDERED_SUBlISTS = 'UNORDERED_SUBLISTS'
    UNORDERED_LIST = 'UNORDERED_LIST'
    EQUAL = 'EQUAL'

def verify(output, answer, verify_method):
    if not hasattr(Verification, verify_method):
        raise ValueError(f"{verify_method} not supported")

    enum_method = getattr(Verification, verify_method)
    if enum_method == Verification.UNORDERED_SUBlISTS:
        return verify_unordered_sublists(output, answer)
    elif enum_method == Verification.EQUAL:
        return output == answer
    elif enum_method == Verification.UNORDERED_LIST:
        return verify_unordered_list(output, answer)
    else:
        raise Exception(f"{enum_method} not supported")

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