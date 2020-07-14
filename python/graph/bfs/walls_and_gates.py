import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def walls_and_gates(self, rooms: List[List[int]]) -> List[List[int]]:
        AROUND = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def get_neighbors(r, c):
            res = []
            for ri, ci in AROUND:
                nr, nc = r + ri, c + ci
                if nr >= 0 and nc >= 0 and nr < len(rooms) and nc < len(rooms[0]) and rooms[nr][nc] != -1:
                    res.append((nr, nc))
            return res

        q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))

        visited = set(q)
        q = collections.deque(q)
        step = 1
        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                for nr, nc in get_neighbors(r, c):
                    if (nr, nc) in visited:
                        continue
                    rooms[nr][nc] = step
                    visited.add((nr, nc))
                    q.append((nr, nc))
            step += 1
        return rooms

"""
286. Walls and Gates
Medium

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
