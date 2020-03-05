import collections
from typing import List

import base.solution

class Solution(base.solution.Solution):
    
    def topsort_basic(self, edges: List[List[int]] = []):
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