import typing

import base.solution

class Solution(base.solution.Solution):

    """
    Bruteforce and adhoc
    """
    def valid_tic_tac_toe_state(self, board: typing.List[str]) -> bool:
        xm = []
        om = []
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == 'X':
                    xm.append((i, j))
                elif c == 'O':
                    om.append((i, j))

        def strike(points):
            rc = [0] * 3
            cc = [0] * 3
            diag = 0
            antd = 0
            for i, j in points:
                rc[i] += 1
                cc[j] += 1
                if i + j == 2: diag += 1
                if i - j + 2 == 2: antd += 1

            return sum([
                len([n for n in rc if n == 3]) > 0,
                len([n for n in cc if n == 3]) > 0,
                diag == 3,
                antd == 3
            ]) 
        
        if len(xm) < len(om) or abs(len(xm) - len(om)) > 1:
            return False

        xs, os = strike(xm), strike(om)
        if xs > 0:
            if xs == os == 1: return False
            if len(xm) == len(om): return False
        if os > 0:
            if len(om) != len(xm): return False
            
        return True

"""
794. Valid Tic-Tac-Toe State
Medium

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""
