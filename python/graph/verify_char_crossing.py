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
        def dfs(curr, side):
            side_state[curr] = side

            for nxt in graph[curr]:
                if nxt in side_state:
                    if side_state[curr] == side_state[nxt]:
                        return False
                else:
                    if not dfs(nxt, not side):
                        return False
            return True

        hm = collections.defaultdict(list)
        for i, c in enumerate(chars):
            hm[c].append(i)

        graph = collections.defaultdict(list)
        for c, (s, e) in hm.items():
            # Get the char between start, end ind with count == 1
            graph[c] = [i for i, count in collections.Counter(chars[s + 1: e]).items() if count == 1]

        if not graph: return True # no crossing

        curr = next(iter(graph))
        side_state = {}
        return dfs(curr, True)
