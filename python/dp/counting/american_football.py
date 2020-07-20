import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def american_football(self, S: int) -> int:
        if S < 0:
            raise ValueError()
        
        now = [0] * (S + 1)
        now[0] = 1
        for n in range(1, S + 1):
            now[n] = (now[n - 2] if now >= 2 else 0) + \
                    (now[n - 3] if now >= 3 else 0) + \
                    (now[n - 6] if now >= 6 else 0)
        return now[s]
    
    # Space optimized O(1)
    def american_football(self, S: int) -> int:
        if S < 0:
            raise ValueError()
        
        now = [0] * 6
        now[0] = 1
 
        for n in range(1, S + 1):
            now[n % 6] = (now[(n - 2) % 6] if n >= 2 else 0) + \
                        (now[(n - 3) % 6] if n >= 3 else 0) + \
                        (now[(n - 6) % 6] if n >= 6 else 0)
        print(now)
        return now[S % 6]


"""
Possible Score: 2, 3, 6
How many ways are there to reach a given score S
S = 7
2 -> 2 -> 3
2 -> 3 -> 2
3 -> 2 -> 2
"""
