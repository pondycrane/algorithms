import typing

import base.solution

class Solution(base.solution.Solution):

    def subset_sum(self, arr: typing.List[int], target: int) -> typing.List[typing.List[int]]:
        result = []
        
        def recursion(state, cur_total, pos):
            if cur_total > target:
                return
            
            if pos == len(arr):
                if cur_total == target:
                    result.append(state[:])
                return
            
            state.append(arr[pos])
            recursion(state, cur_total + arr[pos], pos + 1)
            state.pop()
            recursion(state, cur_total, pos + 1)
            
        recursion([], 0, 0)
        return result

"""
Return all subsets sum up to a target
"""