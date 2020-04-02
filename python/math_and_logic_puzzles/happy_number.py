import base.solution
import math

class Solution(base.solution.Solution):
    def happy_number(self, n: int) -> bool:

        def process(num):
            res = 0
            while num != 0:
                res += int(num % 10) ** 2
                num = math.floor(num / 10)
            return res

        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = process(n) 
        
        return n == 1



"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""