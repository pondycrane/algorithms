import heapq
from typing import List

import base.solution

class Solution(base.solution.Solution):
    def nearest_neighbor(self, p_x, p_y, k, n_points) -> List[List[int]]:
        """
        T: O(NlogK)
        S: O(K)
        """
        def get_dist(x, y):
            return ((x - p_x)**2 + (y - p_y)**2)**0.5
        
        h = []
        for i, (x, y) in enumerate(n_points):
            d = -get_dist(x, y)
            if i < k:
                heapq.heappush(h, (d, (x, y)))
            elif d > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (d, (x, y)))
        return [list(heapq.heappop(h)[1]) for _ in range(k)]
