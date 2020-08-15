import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    T: O(N)
    S: O(N)
    """
    def snakes_and_ladders_matrix(self, n: int, moves: List[int]) -> bool:
        if not moves or len(moves) <= 1:
            return 0
        
        def teleport(s):
            checked = set([s])
            while moves[s] != -1:
                s = moves[s]
                if s in checked:
                    return -1
                checked.add(s)
            return s

        dq = collections.deque([0])
        c = 0
        seen = set()
        while dq:
            l = len(dq)
            c += 1
            for _ in range(l):
                s = teleport(dq.popleft())
                if s == -1:
                    continue
                
                seen.add(s)
                
                next_steps = []
                non_portal_found = False
                for i in range(6, 0, -1):
                    if s + i >= n:
                        continue
                    
                    if moves[s + i] != -1:
                        next_steps.append(i)
                    elif not non_portal_found:
                        next_steps.append(i)
                        non_portal_found = True
                    
                for i in next_steps:
                    ns = teleport(s + i)
                    if ns == -1:
                        continue
                    
                    if ns == n - 1:
                        return c
                    
                    if ns not in seen:
                        dq.append(ns)
        return -1


"""
Need to go from first point to last point.
Any value not -1 is a portal to the index value its pointing.
"""
