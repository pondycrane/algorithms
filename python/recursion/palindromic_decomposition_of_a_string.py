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

    """
    DP solution, and use list rather than string
    """
    def palindromic_decomposition_of_a_string(self, s: str) -> typing.List[str]:
        result = []

        memo = {}
        def ispalindrom(left, right):
            key = (left, right)
            if key in memo:
                return memo[key]
            
            while left < right:
                if s[left] != s[right]:
                    memo[(left, right)] = False
                    memo[key] = False
                    return memo[key]
                left += 1
                right -= 1
            memo[key] = True
            return memo[key]

        memo2 = {}
        def valid_palindroms(pos):
            if pos in memo2:
                return memo2[pos]
            
            if pos == len(s):
                return []
            
            res = []
            for j in range(pos, len(s)):
                if ispalindrom(pos, j):
                    substr = s[pos: j + 1]
                    next_vp = valid_palindroms(j + 1)
                    if not next_vp:
                        res.append(substr)
                    else:
                        res.extend([
                            f'{substr}|{string}' for string in next_vp
                        ])
            
            memo2[pos] = res
            return memo2[pos]
            
        return valid_palindroms(0)
