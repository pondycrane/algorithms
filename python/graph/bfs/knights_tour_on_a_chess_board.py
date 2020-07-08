import collections
from typing import List

import base.solution


"""
Walk a Knight from point a to point b, find minimum step
"""
class Solution(base.solution.Solution):
    def knights_tour_on_a_chess_board(self, rows: int, cols: int, start_row: int, start_col: int, end_row: int, end_col: int):
        def is_valid(nr, nc):
            return nr >= 0 and nc >= 0 and nr < rows and nc < cols and (nr, nc) not in visited

        def get_neighbors(r, c):
            res = []
            for i in [2, -2]:
                for j in [1, -1]:
                    nr, nc = r + i, c + j
                    if is_valid(nr, nc): res.append((nr, nc))
                    nr, nc = r + j, c + i
                    if is_valid(nr, nc): res.append((nr, nc))
            return res

        start_cord = (start_row, start_col)
        q = collections.deque([start_cord])
        visited = set([start_cord])
        mc = 0
        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                if r == end_row and c == end_col: return mc
                for neighbor in get_neighbors(r, c):
                    q.append(neighbor)
                    visited.add(neighbor)
            mc += 1
        return -1
