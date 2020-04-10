
import base.solution

class Solution(base.solution.Solution):
    def backspace_string_compare(self, S: str, T: str) -> bool:
        def get_result(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        return get_result(S) == get_result(T)
    
    """
    Can you get O(1) space complexity?
    """
    def backspace_string_compare(self, S: str, T: str) -> bool:
        p1 = len(S) - 1
        p2 = len(T) - 1

        def forward_ind(ind, string):
            bs = 0
            while ind >= 0 and (bs > 0 or string[ind] == '#'):
                if string[ind] == '#':
                    bs += 1
                else:
                    bs -= 1
                ind -= 1
            return ind

        while p1 >= 0 and p2 >= 0:
            p1 = forward_ind(p1, S)
            p2 = forward_ind(p2, T)

            if p1 < 0 and p2 < 0:
                return True
            
            if S[p1] != T[p2]:
                return False
            p1 -= 1
            p2 -= 1
        
        return forward_ind(p1, S) == forward_ind(p2, T) == -1

            
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""