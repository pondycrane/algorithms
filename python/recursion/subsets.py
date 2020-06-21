import typing

import base.solution

class Solution(base.solution.Solution):

    def subsets(self, arr: typing.List[int]) -> typing.List[typing.List[int]]:
        result = []
        def recursion(curr, ind):
            if ind == len(arr):
                nonlocal result
                result = curr
                return
            

            copied = curr.copy()
            recursion(curr + [
                l + [arr[ind]] for l in curr
            ], ind + 1)
        
        recursion([[]], 0)
        return result
    
    def subsets(self, arr: typing.List[int]) -> typing.List[typing.List[int]]:
        result = []
        def recursion(slate, ind):
            if ind == len(arr):
                result.append(slate.copy())
                return
            
            # Take
            slate.append(arr[ind])
            recursion(slate, ind + 1)
            # Not take
            slate.pop()
            recursion(slate, ind + 1)
        
        recursion([], 0)
        return result