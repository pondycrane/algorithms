import itertools
import base.solution

class Solution(base.solution.Solution):
    def add_strings(self, num1: str, num2: str) -> str:
        base = ord('0')
        carry = 0
        result = []
        
        def num_gen(num1, num2):
            return itertools.zip_longest(reversed(num1), reversed(num2), fillvalue='0')
        
        for n1, n2 in num_gen(num1, num2):
            sumord = (ord(n1) + ord(n2)) % base + carry
            result.append(str(sumord % 10))
            carry = sumord // 10
        
        if carry > 0:
            result.append(str(carry))
        
        return ''.join(reversed(result))




"""
415. Add Strings
Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""