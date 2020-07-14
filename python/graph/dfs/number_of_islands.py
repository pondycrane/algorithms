import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def number_of_islands(self, grid: List[List[str]]) -> int:
        def get_neighbors(r, c):
            res = []
            for ir, ic in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + ir, c + ic
                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == '1':
                    res.append((nr, nc))
            return res

        def dfs(i, j):
            if grid[i][j] == '0': return
            grid[i][j] = '0'
            for nr, nc in get_neighbors(i, j):
                dfs(nr, nc)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    island_count += 1
        return island_count


"""
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
