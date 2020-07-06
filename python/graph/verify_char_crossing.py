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
    """
    def verify_char_crossing(self, chars: str) -> bool:

