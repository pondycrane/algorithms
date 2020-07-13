import collections
from typing import List
from enum import Enum

import base.solution

class Status(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Solution(base.solution.Solution):
    def graph_valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        status = [Status.UNVISITED for _ in range(n)]
        def is_acyclic(v, parent):
            status[v] = Status.VISITING
            for nv in g[v]:
                if status[nv] is Status.UNVISITED and not is_acyclic(nv, v):
                    return False
                elif status[nv] is Status.VISITING:
                    if nv == parent:
                        continue
                    return False
            status[v] = Status.VISITED
            return True
        
        if not is_acyclic(0, -1):
            return False

        for state in status:
            if state is Status.UNVISITED:
                return False
        return True

"""
261. Graph Valid Tree
Medium

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
