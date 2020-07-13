import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def shortest_path_in_binary_matrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1]:
            return -1

        AROUND = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def get_neighbors(r, c):
            res = []
            for ri, ci in AROUND:
                nr, nc = r + ri, c + ci
                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 0:
                    res.append((nr, nc))
            return res

        visited = [[False] * len(row) for row in grid]
        q = collections.deque([(0, 0)])
        visited[0][0] = True
        count = 1
        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()

                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return count

                for nr, nc in get_neighbors(r, c):
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            count += 1
        return -1

"""
1091. Shortest Path in Binary Matrix
Medium

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
"""
        
