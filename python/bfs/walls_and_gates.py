import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def walls_and_gates(self, rooms: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        steps = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        def is_valid(x, y):
            if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]) or rooms[x][y] != float('inf'):
                return False
            return True

        while queue:
            x, y = queue.popleft()
            for ix, iy in steps:
                nx, ny = x + ix, y + iy
                if is_valid(nx, ny):
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))
        return rooms



"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

1. -1 - A wall or an obstacle.
2. 0 - A gate.
3. INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
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