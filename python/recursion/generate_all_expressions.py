import typing

import base.solution

class Solution(base.solution.Solution):

    """
    Bruteforce, works but too slow
    T: O(3**N)
    S: O(N)
    """
    def generate_all_expressions(self, s: str, target: int) -> typing.List[str]:
        operations = ['+', '*']
        result = []
        
        def evaluate(string) -> int:
            while '*' in string:
                ind = string.index('*')
                left = ind - 1
                while left >= 0 and string[left].isnumeric():
                    left -= 1
                right = ind + 1
                while right < len(string) and string[right].isnumeric():
                    right += 1
                total = int(string[left + 1: ind]) * int(string[ind + 1: right])
                string = string[:left + 1] + str(total) + string[right:]
            return sum(map(int, string.split('+')))
            
        def recursion(slate, pos):
            if pos == len(s):
                st = ''.join(slate)
                if evaluate(st) == target:
                    result.append(st)
                return
            
            if slate and slate[-1].isnumeric():
                for op in operations:
                    slate.append(op)
                    recursion(slate, pos)
                    slate.pop()
            
            slate.append(s[pos])
            recursion(slate, pos + 1)
            slate.pop()
            
        recursion([], 0)
        return result
    
    """
    With backgracking. To add backtracking, we save the current
    sum as attribute. We also save prev value for multiplication use.
    """
    def generate_all_expressions(self, s: str, target: int) -> typing.List[str]:
        result = []
        def recursion(slate, pos, cur_sum, prev):
            # Backtracking, check 0 in case the value decrease
            if 0 < target < cur_sum and '0' not in s[pos:]:
                return

            # Base case
            if pos == len(s):
                if cur_sum == target:
                    result.append(slate)
                return
            
            for j in range(pos, len(s)):
                intstr = s[pos:j + 1]
                integer = int(intstr)
                if pos == 0:
                    # operators cannot be the start
                    recursion(intstr, j + 1, integer, integer)
                else:
                    # use +
                    recursion(slate + '+' + intstr, j + 1, cur_sum + integer, integer)
                    # use *
                    recursion(slate + '*' + intstr, j + 1, cur_sum - prev + prev * integer, prev * integer)

        recursion('', 0, 0, 0)
        return result