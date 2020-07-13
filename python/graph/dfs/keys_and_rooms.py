import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def keys_and_rooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            for nv in rooms[v]:
                dfs(nv)

        dfs(0)
        return len(visited) == len(rooms)
