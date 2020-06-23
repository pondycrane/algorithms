import typing

import base.solution

class Solution(base.solution.Solution):
    """
    T: O(N**N)
    S: O(N)
    """
    def palindromic_decomposition_of_a_string(self, s: str) -> typing.List[str]:
        result = []
        
        def ispalindrom(string):
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def recursion(slate, pos):
            # Basecase
            if pos == len(s):
                result.append(slate)
                return
            
            for j in range(pos, len(s)):
                substr = s[pos:j + 1]
                # Backtracking
                if ispalindrom(substr):
                    if pos == 0:
                        recursion(substr, j + 1)
                    else:
                        recursion(slate + '|' + substr, j + 1)
            
        recursion('', 0)
        return result