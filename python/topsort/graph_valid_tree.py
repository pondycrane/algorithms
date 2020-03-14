import collections
import typing
import base.solution

class Solution(base.solution.Solution):
    def graph_valid_tree(self, n: int, edges: typing.List[typing.List[int]]):
        if not edges:
            return n < 2
        
        visited = [0] * n
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def is_cycle(node, prev):
            visited[node] = 1
            for next_n in graph[node]:
                if next_n == prev:
                    continue
                
                if visited[next_n] == 1:
                    return True
                
                if is_cycle(next_n, node):
                    return True
            visited[node] = 2
            return False
        

        if is_cycle(list(graph.keys())[0], -1):
            return False 
        else:
            return sum(visited) == (n * 2)
        





"""
261. Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""