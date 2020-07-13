import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    DFS top down
    """
    def evaluate_division(self, equations: List[List[str]], values: List[float], equations: List[List[str]]) -> List[float]:
        g = collections.defaultdict(lambda: collections.defaultdict(float))
        for i, (s, d) in enumerate(equations):
            g[d][s] = values[i]
            g[s][d] = 1 / values[i]

        def dfs(v, target, cur, visited):
            if v in visited: return -1
            if v not in g: return -1 
            visited.add(v)
            if v == target:
                return cur
            for nv, nw in g[v].items():
                res = dfs(nv, target, cur * nw, visited)
                if res != -1: return res
            return -1 # If the value can be negative, we can return a tuple like (found, val)
        
        res = []
        for s, d in queries:
            res.append(dfs(d, s, 1, set()))

        return res


    """
    DFS bottom up
    """
    def evaluate_division(self, equations: List[List[str]], values: List[float], equations: List[List[str]]) -> List[float]:
        g = collections.defaultdict(lambda: collections.defaultdict(float))
        for i, (s, d) in enumerate(equations):
            g[d][s] = values[i]
            g[s][d] = 1 / values[i]

        def dfs(v, target, cur, visited):
 
