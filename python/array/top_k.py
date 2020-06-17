import heapq
import typing

import base.solution

class Solution(base.solution.Solution):
    def top_k(self, arr, k) -> typing.List[int]:
        arr = list(set(arr))
        heap = arr[:k]
        heapq.heapify(heap)
        for i in range(k, len(arr)):
            heapq.heappushpop(heap, arr[i])
        return heap