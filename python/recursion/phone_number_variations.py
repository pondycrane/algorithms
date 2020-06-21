import typing

import base.solution

class Solution(base.solution.Solution):

    def phone_number_variations(self, num: str) -> typing.List[str]:
        if '0' in num:
            return []

        def get_chars(digit):
            int_form = int(digit) - 1
            return [chr(int(i) + ord('a')) for i in range(int_form * 3, int_form * 3 + 3) if i < 26]

        result = []
        def recursion(state, pos):
            if pos == len(num):
                result.append(''.join(state))
                return
            
            for c in get_chars(num[pos]):
                state.append(c)
                recursion(state, pos + 1)
                state.pop()
        
        recursion([], 0)
        return result
        
