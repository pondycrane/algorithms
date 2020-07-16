import collections
from typing import List

import base.solution
from lib.ds_collections.treenode import TreeNode


class Solution(base.solution.Solution):
    """
    Recursive DFS
    """
    def critical_connections(self, noOfServers: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)

        def dfs(v, parent):
            if v in dist:
                return
            dist[v] = 0 if parent is None else dist[parent] + 1
            low[v] = dist[v]
            for nv in g[v]:
                if nv == parent: continue
                if nv not in dist:
                    dfs(nv, v)
                low[v] = min(low[nv], low[v])
                if low[nv] > low[v]:
                    res.append([v, nv])

        low, dist, res = {}, {}, []
        for i in range(noOfServers):
            dfs(i, None)
        
        return [[-1, -1]] if not res else res

    """
    Iterative DFS
    """
    def critical_connections(self, noOfServers: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)

        low, dist, parent = {}, {}, collections.defaultdict(lambda: None)
        visited = [False] * noOfServers
        for v in range(noOfServers):
            if not visited[v]:
                s1, s2 = [v], []
                dist[v] = low[v] = 0
                while s1:
                    cv = s1.pop()
                    s2.append(cv)
                    visited[cv] = True
                    for nv in g[cv]:
                        if nv == parent[cv]: continue
                        if visited[nv]: continue
                        parent[nv] = cv
                        dist[nv] = low[nv] = dist[cv] + 1
                        s1.append(nv)
                while s2:
                    cv = s2.pop()
                    for nv in g[cv]:
                        if nv == parent[cv]: continue
                        low[cv] = min(low[nv], low[cv])
        res = []
        for v in range(noOfServers):
            ans = parent[v]
            if ans is not None and low[v] > dist[ans]:
                res.append([ans, v])
        return [[-1, -1]] if not res else res


"""
Find the critical connections that, once removed, can disconnect two nodes in a graph.
"""
