import typing

import base.solution

class Solution(base.solution.Solution):

    def permutations(self, arr: typing.List[int]) -> typing.List[typing.List[int]]:
        result = []
        def recursion(slate, arr):
            if not arr:
                result.append(slate.copy())
                return
            
            for i, num in enumerate(arr):
                slate.append(num)
                recursion(slate, arr[:i] + arr[i + 1:])
                slate.pop()
        
        recursion([], arr)
        return result

    # better way, memory efficient
    # anything before pos is fixed slate, and we use swap as
    # way to iterate anything after pos
    def permutations(self, arr: typing.List[int]) -> typing.List[typing.List[int]]:
        result = []
        def permutations(pos):
            if pos == len(arr):
                result.append(arr[:])
                return
            
            for i in range(pos, len(arr)):
                arr[pos], arr[i] = arr[i], arr[pos]
                permutations(pos + 1)
                arr[pos], arr[i] = arr[i], arr[pos]
        
        permutations(0)
        return result