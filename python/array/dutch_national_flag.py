import typing

import base.solution

class Solution(base.solution.Solution):
    def dutch_national_flag(self, balls: typing.List[str]) -> typing.List[str]:
        if not balls or len(balls) <= 1:
            return balls
        
        r, g, b = 0, 0, len(balls) - 1
        while g <= b:
            if balls[g] == 'G':
                g += 1
            elif balls[g] == 'R':
                balls[r], balls[g] = balls[g], balls[r]
                r += 1
                g += 1
            elif balls[g] == 'B':
                balls[g], balls[b] = balls[b], balls[g]
                b -= 1
        return balls
