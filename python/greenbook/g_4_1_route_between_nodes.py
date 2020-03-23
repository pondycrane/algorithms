import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def g_4_1_route_between_nodes(self, edges: typing.List, s: int, e: int) -> bool:
        graph = collections.defaultdict(list)
        seen = collections.defaultdict(bool)
        for a, b in edges:
            seen[a]
            seen[b]
            graph[a].append(b)
            graph[b].append(a)
        
        queue = collections.deque([s])
        found = False
        while queue:
            node = queue.popleft()
            if node == e:
                found = True
                break
            
            if seen[node]:
                continue
            
            seen[node] = True
            for next_n in graph[node]:
                if not seen[next_n]:
                    queue.append(next_n)
        
        return found


"""
4.1 Route Between Nodes: Given a directed graph and two nodes (S and E), 
deign an algorithm to find out whether there is a route from S to E.

Hank's note: The solution from the book includes 3 states for the node: 
    Visited, Visiting, Unvisited. However, here we only use 2 states by ignoring
    Visiting, since Visiting is only useful when we want to detect cyclic loops.
"""