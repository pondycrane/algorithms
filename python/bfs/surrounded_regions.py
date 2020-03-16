import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def surrounded_regions(self, board: typing.List[typing.List[str]]) -> typing.List[typing.List[str]]:
        if not board:
            return
            
        masked = [
            [False] * len(board[0]) for _ in range(len(board))
        ]
        steps = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        def mask(x, y):
            queue = collections.deque([(x, y)])
            
            while queue:
                x, y = queue.popleft()
                if masked[x][y]:
                    continue
                
                masked[x][y] = True
                for ix, iy in steps:
                    nx, ny = x + ix, y + iy
                    if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]) and board[nx][ny] == 'O' and not masked[nx][ny]:
                        queue.append((nx, ny))
            return
        
        for j in range(len(board[0])):
            if board[0][j] == 'O' and not masked[0][j]:
                mask(0, j)
            if board[len(board) - 1][j] == 'O' and not masked[len(board) - 1][j]:
                mask(len(board) - 1, j)
        for i in range(len(board)):
            if board[i][0] == 'O' and not masked[i][0]:
                mask(i, 0)
            if board[i][len(board[0]) - 1] == 'O' and not masked[i][len(board[0]) - 1]:
                mask(i, len(board[0]) - 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and not masked[i][j]:
                    board[i][j] = 'X'
        return board



"""
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""