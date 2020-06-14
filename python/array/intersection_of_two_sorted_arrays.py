import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def intersection_of_two_sorted_arrays(self, l1: typing.List[str], l2: typing.List[str]) -> typing.List[int]:
        p1, p2, n, m = 0, 0, len(l1), len(l2)
        result = set()
        while True:
            if l1[p1] == l2[p2]:
                result.add(l1[p1])

                p1, p2 = p1 + 1, p2 + 1
                if p1 >= m or p2 >= n:
                    break
                
            elif l1[p1] < l2[p2]:
                p1 += 1
                if p1 >= m:
                    break
            else:
                p2 += 1
                if p2 >= n:
                    break
        
        return list(result)