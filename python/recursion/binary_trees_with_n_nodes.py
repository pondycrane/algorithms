import typing

import base.solution

class Solution(base.solution.Solution):
    """
    memo top down
    """
    def binary_trees_with_n_nodes(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def dfs(n):
            if n in memo:
                return memo[n]
            total = 0
            for i in range(1, n + 1):
                total += dfs(i - 1) * dfs(n - i)
            memo[n] = total
            return memo[n]
        
        return dfs(n)
    
    """
    bottom up
    """
    def binary_trees_with_n_nodes(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                memo[i] += memo[j - 1] * memo[i - j]
        return memo[n]