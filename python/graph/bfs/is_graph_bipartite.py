import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    BFS
    """
    def is_graph_bipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return True

        partite = {}
        for i in range(len(graph)):
            if i not in partite:
                q = collections.deque([i])
                partite[i] = True
                while q:
                    l = len(q)
                    for _ in range(l):
                        v = q.popleft()
                        for nv in graph[v]:
                            if nv in partite:
                                if partite[nv] == partite[v]:
                                    return False
                            else:
                                partite[nv] = not partite[v]
                                q.append(nv)
        return True

    """
    DFS
    """
    def is_graph_bipartite(self, graph: List[List[int]]) -> bool:
        partite = {}
        def dfs(v, part):
            if v in partite:
                return partite[v] == part
            partite[v] = part
            for nv in graph[v]:
                if not dfs(nv, not part):
                    return False
            return True

        for i in range(len(graph)):
            if i not in partite and not dfs(i, True):
                return False
        return True


"""
785. Is Graph Bipartite?
Medium

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""