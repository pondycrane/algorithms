import typing

import base.solution

class Solution(base.solution.Solution):
    def all_upper_lower_words(self, string: str) -> typing.List[str]:
        if not string:
            return []
        
        result = []
        def recursion(curr):
            i = len(curr)
            if i == len(string):
                result.append(''.join(curr))
                return
            
            l = [string[i].lower()]
            if string[i].isalpha():
                l.append(string[i].upper())

            for c in l:
                curr.append(c)
                recursion(curr)
                curr.pop()
        
        recursion([])
        return result

"""
Given a string, return all enumeration of upper and lower cases of the string.
Input: 'a1b1'
Output: ['a1b1', 'a1B1', 'A1b1', 'A1B1']
"""