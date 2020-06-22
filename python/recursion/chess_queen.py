import typing

import base.solution

class Solution(base.solution.Solution):
    def chess_queen(self, queen: int, board: int) -> typing.List[typing.List[typing.List[str]]]:
        # Intuition: 
        #     1. cannot place queen in the same row
        #     2. use list to store where the queen is placed (value = row index)
        result = []

        def valid_queens(x1, y1, x2, y2):
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
            return True
        
        def last_valid(cols):
            if cols[-1] == -1:
                return True
            for ind, li in enumerate(cols[:-1]):
                if valid_queens(ind, li, len(cols) - 1, cols[-1]) == False:
                    return False
            return True
        
        def cols_2_board(cols):
            res = []
            for queens in cols:
                chessres = []
                for r in range(0, board):
                    chessres.append(
                        ''.join(['Q' if r < len(queens) and queens[r] == i else '.' for i in range(board)])
                    )
                res.append(chessres)
            return res

        def n_queens(cols, index):
            # Back tracing
            if cols and last_valid(cols) == False:
                return
            
            # Base case
            if queen > 0 and index == queen:
                result.append(cols[:])
                return
            if len(cols) == board:
                return
            
            # Use queen
            for i in range(0, board):
                cols.append(i)
                n_queens(cols, index + 1)
                cols.pop()
            # Not use queen
            cols.append(-1)
            n_queens(cols, index)
            cols.pop()
            
        n_queens([], 0)
        return cols_2_board(result)
        
        

        