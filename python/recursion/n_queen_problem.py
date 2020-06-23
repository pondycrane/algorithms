import typing

import base.solution

class Solution(base.solution.Solution):
    def n_queen_problem(self, n: int) -> typing.List[typing.List[str]]:
        if not n:
            return []

        result = []
        def is_valid(r, c):
            if cols_used[c] or diag_used[r + c] or antd_used[r - c + n]:
                return False
            return True

        def visualize(slate):
            res = []
            for c in slate:
                res.append(''.join(['q' if i == c else '-' for i in range(n)]))
            return res
        
        cols_used = [False] * n
        diag_used = [False] * (2 * n)
        antd_used = [False] * (2 * n)
        def recursion(slate):
            if len(slate) == n:
                result.append(visualize(slate))
            
            for c in range(n):
                if is_valid(len(slate), c):
                    cols_used[c] = True
                    diag_used[len(slate) + c] = True
                    antd_used[len(slate) - c + n] = True
                    slate.append(c)
                    recursion(slate)
                    slate.pop()
                    cols_used[c] = False
                    diag_used[len(slate) + c] = False
                    antd_used[len(slate) - c + n] = False
        
        recursion([])
        return result