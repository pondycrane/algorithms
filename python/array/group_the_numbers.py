import typing

import base.solution

class Solution(base.solution.Solution):
    def group_the_numbers(self, arr: typing.List[int]) -> typing.List[int]:
        """
        Basically using the partition strategy in quicksort.
        """
        j = 0
        for i in range(0, len(arr)):
            if arr[i] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return arr

"""
Rearrange the array to even at front, odd at rear.
The order doesn't matter.
"""