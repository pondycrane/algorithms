import typing

import base.solution

class Solution(base.solution.Solution):
    def numIslands(self, grid: typing.List[List[str]]) -> int:
        STEPS = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
