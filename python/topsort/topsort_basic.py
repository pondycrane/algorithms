import collections
from typing import List

import base.solution

class GNode:
    def __init__(self):
        self.incoming_count = 0
        self.children = []

class Solution(base.solution.Solution):
    """
    Use Topological sort to go through all DAG nodes. Any non DAG node will not
    go through BFS.
    T: O(N)
    S: O(N), using a set to track
    """
    def topsort_basic(self, edges: List[List[int]] = []):
        if type(edges) is not list:
            raise TypeError(f"Input type error {type(edges)}")
        
        graph = collections.defaultdict(GNode)
        all_nodes = set()
        for a, b in edges:
            graph[a].children.append(b)
            graph[b].incoming_count += 1
            all_nodes.add(graph[a])
            all_nodes.add(graph[b])

        queue = collections.deque()
        for node in graph.values():
            if node.incoming_count == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            for n_node in node.children:
                graph[n_node].incoming_count -= 1
                if graph[n_node].incoming_count == 0:
                    queue.append(graph[n_node])
            if node in all_nodes:
                all_nodes.remove(node)

        return len(all_nodes) == 0
    
    """
    Using set to track each dfs, and detect circle if next step in set.
    T: O(N)
    S: O(N)
    """
    def topsort_basic_with_set_approach(self, edges: List[List[int]] = []):
        if type(edges) is not list:
            raise TypeError(f"Input type error {type(edges)}")
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        # Track total visit, just like regular topsort
        visited = set()

        def dfs(curr_visited, visiting):
            curr_visited.add(visiting)
            is_dag = True

            if visiting not in graph:
                # Leaf node detected
                curr_visited.remove(visiting)
                return is_dag
            
            for next_visit in graph[visiting]:
                # Loop detected
                if next_visit in curr_visited:
                    is_dag = False
                    break
                
                if next_visit not in visited:
                    curr_visited.add(next_visit)
                    # Loop detected, back track
                    if not dfs(curr_visited, next_visit):
                        is_dag = False
                        break
            
            curr_visited.remove(visiting)
            return is_dag
            
        for course in graph:
            if course not in visited:
                if not dfs(set(), course): # Use set to track loop
                    return False
        return True