import collections

import base.solution

class Solution(base.solution.Solution):
    
    def topsort_basic(self, data):
        graph = collections.defaultdict(list)
        for a, b in data:
            graph[a].append(b)
        
        # Track total visit, just like regular topsort
        visited = set()

        def dfs(curr_visited, cur_visit):
            if cur_visit not in graph:
                return True
                
            for next_visit in graph[cur_visit]:
                if next_visit in curr_visited:
                    return False
                
                if next_visit not in visited:
                    curr_visited.add(next_visit)
                    if not dfs(curr_visited, next_visit):
                        return False
            return True

        for course in graph:
            if course not in visited:
                if not dfs(set([course]), course): # Use set to track loop
                    return False
        return True