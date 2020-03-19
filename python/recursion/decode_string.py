import base.solution

class Solution(base.solution.Solution):
    def decode_string(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == ']':
                chars = []
                while stack and stack[-1] != '[':
                    chars.append(stack.pop())
                
                stack.pop()
                digits = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                stack.append(int(''.join(digits[::-1])) * ''.join(chars))
            else:
                stack.append(s[i])
        stack.reverse()
        return ''.join(stack)[::-1]




"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""