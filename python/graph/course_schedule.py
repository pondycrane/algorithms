import collections
from typing import List

import base.solution


"""
You are given a list of course dependencies, find the courses need to take.
Input: list of dependences. [a, b] means class a depends on finishing class b.
"""
class Solution(base.solution.Solution):
    """
    Kuhn's algorithm
    """
    def course_schedule(self, dependencies: List[List[int]] = []):
        depmap = collections.defaultdict(int)
        g = collections.defaultdict(list)
        for a, b in dependencies:
            depmap[a] += 1
            depmap[b]
            g[b].append(a)
        
        sources = [v for v, c in depmap.items() if c == 0]
        q = collections.deque(sources)
        for s in sources: del depmap[s]
        while q:
            v = q.popleft()
            for nv in g[v]:
                depmap[nv] -= 1
                if depmap[nv] == 0:
                    q.append(nv)
                    del depmap[nv]
        return len(depmap) == 0

    """
    Topsort
    """
    def course_schedule(self, dependencies: List[List[int]] = []):
        g = collections.defaultdict(list)
        for a, b in dependencies:
            g[a].append(b)
            g[b]
        
        def dfs(v):
            if visited[v] == 1: return True
            if visited[v] == -1: return False
            visited[v] = -1
            for nv in g[v]:
                if not dfs(nv): return False
            visited[v] = 1
            return True
        
        visited = collections.defaultdict(int)
        for v in g:
            if not dfs(v): return False

        return True
