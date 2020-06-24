import itertools

import base.solution

class Solution(base.solution.Solution):

    def zigzag_conversion(self, s: str, numRows: int) -> str:
        if not s or len(s) <= 2:
            return s
        
        def get_unit(n):
            if n == 1:
                return 1
            return n * 2 - 2
        
        def horiz_gen(string, unit):
            l, r = 0, unit - 1
            
            while l < len(string) and l < r:
                if l == 0:
                    yield string[l]
                    l += 1
                else:
                    yield string[l] + (string[r] if r < len(string) else '')
                    l += 1
                    r -= 1
            if l == r and l < len(string):
                yield string[l]
        
        res = []
        unit = get_unit(numRows)
        gens = [horiz_gen(s[i:i + unit], unit) for i in range(0, len(s), unit)]
        zipped = itertools.zip_longest(*gens, fillvalue='')
        for strings in zipped:
            res.append(''.join(list(strings)))
        return ''.join(res)


"""
ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""