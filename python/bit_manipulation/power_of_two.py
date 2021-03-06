import base.solution

class Solution(base.solution.Solution):
    """
    T: O(N)
    """
    def power_of_two(self, n: int) -> bool:
        if n <= 0:
            return False
        
        one_count = 0
        while n != 0:
            one_count += n & 1
            n >>= 1
        return one_count == 1
    
    """
    Turn the right-most bit to 0: Since the solution only has
    1 bit, turnning the right-most bit to 0 leads to 0 value.
    x & (x - 1)

    T: O(1)
    """
    def power_of_two(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0



"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2**0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2**4 = 16
Example 3:

Input: 218
Output: false
"""