import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def word_search(self, board: List[List[str]], word: str) -> bool:
        def get_neighbors(r, c):
            res = []
            for ir, ic in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + ir, c + ic
                if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]):
                    res.append((nr, nc))
            return res

        def dfs(r, c, wind):
            if board[r][c] != word[wind]:
                return False
            if wind == len(word) - 1:
                return True

            board[r][c] = '?'
            for nr, nc in get_neighbors(r, c):
                if dfs(nr, nc, wind + 1):
                    return True
            board[r][c] = word[wind]
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

"""
79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
