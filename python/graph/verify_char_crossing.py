import collections
from typing import List

import base.solution


"""
You are given a string with each charactor showing up twice. You need to identify
whether the string is valid. If the bridging of each type of character will cross other characters, then he string is invalid.

Input: "abcabc"
Output: False
Explination: There's no way of connecting these chars without the bridge crossing each other.
   _____
  |     |
  a b c a b c
    |_|____||
      |_____|

Input: "dabebcadce"
Output: True
Explination:

   _____________
  |  _________  |
  | |  ___    | |
  | | |   |   | |
  d a b e b c a d c e
        |   |_____| |
        |___________|
"""
class Solution(base.solution.Solution):
    """
    Intuition. Need to identify the key relationship between chars that makes this problem a graph problem.
    Dependency can be identified if all bridges are on the same side. For case 2,
    bridge d depends on the bridges of e and c;
    bridge a depends on the bridges of e and c;
    bridge b depends on the bridge of e;
    bridge e depends on the bridges of d, a, and b;
    bridge c depends on the bridges of a and d;
    bridge a depends on the bridges of c and e;
         ___________
   _____|_______    |
  |  ___|_____  |   |
  | |  _|_   _|_|_  |
  | | | | | | | | | |
  d a b e b c a d c e

    a graph can be built: {'d': ['e', 'c'], 'a': ['e', 'c'], 'b': ['e'], 'e': ['b', 'a', 'd'], 'c': ['a', 'd']}
    
    We know that each adjecent vectors are compatible if they are on different sides.
    We can confirm with a BFS walk, and check the current vector has the opposite sign of its parent, and no collusion is found.
    """
    def verify_char_crossing(self, chars: str) -> bool:
        indmap = collections.defaultdict(list)
        graph = collections.defaultdict(list)
        for i, c in enumerate(chars):
            indmap[c].append(i)
        
        for c, (s, e) in indmap.items():
            # Get the char between start, end ind with count == 1
            graph[c] = [cn for cn, count in collections.Counter(chars[s + 1: e]).items() if count == 1]
        if not graph:
            return True

        # Start bfs, make sure each adj vector has different mark
        # 1 should have an adj vector of 0, and 0 should have an adj vector of 1
        starter = next(iter(graph))
        q = collections.deque([starter])
        state = {starter: True}
        while q:
            c = q.popleft()
            for nc in graph[c]:
                if nc in state:
                    if state[nc] == state[c]:
                        return False
                else:
                    state[nc] = not state[c]
                    q.append(nc)
        return True





