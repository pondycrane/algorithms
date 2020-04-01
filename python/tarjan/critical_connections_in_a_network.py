import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def critical_connections_in_a_network(self, connections: typing.List[typing.List[int]]) -> typing.List[int]:
        graph = collections.defaultdict(lambda: set())
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        
        ids = {}
        best = {}
        critical_connections = []
        self.count = 0
        def dfs(prev, node):
            if node in ids:
                return
            
            ids[node] = self.count
            best[node] = self.count
            self.count += 1
            for next_n in graph[node]:
                if next_n == prev:
                    continue
                
                dfs(node, next_n)
                if best[next_n] > ids[node]:
                    critical_connections.append([node, next_n])
                
                best[node] = min(best[node], best[next_n])
        
        for node in list(graph.keys()):
            dfs(-1, node)
        
        return critical_connections


"""
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.


Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
"""