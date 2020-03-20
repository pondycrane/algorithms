import base.solution

class Solution(base.solution.Solution):
    def remove_invalid_parentheses(self, s: str) -> str:
        def is_valid(s):
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                    if left < 0:
                        return False
            return left == 0
        
        res = []
        min_depth = [float('inf')]
        memo = set()
        def dfs(s, depth):
            if s in memo:
                return
            if len(res) > 0 and depth > min_depth[0]:
                return
            
            memo.add(s)
            if is_valid(s):
                if depth < min_depth[0]:
                    min_depth[0] = depth
                    res.clear()
                
                res.append(s)
            else:
                for i in range(len(s)):
                    if s[i] in ['(', ')']:
                        dfs(s[0:i] + s[i + 1:], depth + 1)
        
        dfs(s, 0)
        return res

"""
301. Remove Invalid Parentheses
Hard

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""