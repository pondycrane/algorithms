import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    DFS top down
    """
    def evaluate_division(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
    def evaluate_division(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = collections.defaultdict(lambda: collections.defaultdict(float))
        for i, (s, d) in enumerate(equations):
            g[d][s] = values[i]
            g[s][d] = 1 / values[i]

        def dfs(v, target):
            if v in visited:
                return -1
            visited.add(v)
            to_return = -1
            for nv, nw in g[v].items():
                if nv == target:
                    to_return = nw
                    break
                cures = dfs(nv, target)
                if cures != -1:
                    to_return = nw * cures
                    break
            visited.remove(v)
            return to_return

        res = []
        visited = set()
        for d, s in queries:
            res.append(dfs(s, d))
        return res
"""
399. Evaluate Division
Medium

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
