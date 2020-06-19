import bisect
import typing

import base.solution

class Solution(base.solution.Solution):
    def nuts_and_bolts(self, nuts: typing.List[str], bolts: typing.List[str]) -> typing.List[typing.List[str]]:
        def partition(start, end, arr, pivot):
            if start == end:
                return start
            
            j = i = start
            count = 0
            while j < end:
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j += 1
                elif arr[j] == pivot:
                    arr[j], arr[end] = arr[end], arr[j]
                else:
                    j += 1
            arr[end], arr[i] = arr[i], arr[end]
            return i
        
        def quicksort_helper(start, end):
            if start >= end:
                return
            
            pivot = partition(start, end, nuts, nuts[end])
            pivot = partition(start, end, bolts, nuts[pivot])
            quicksort_helper(start, pivot - 1)
            quicksort_helper(pivot + 1, end)


        quicksort_helper(0, len(nuts) - 1)
        return [nuts, bolts]
