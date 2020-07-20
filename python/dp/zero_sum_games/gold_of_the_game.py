import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def gold_of_the_game(self, bags: List[int]) -> int:
        dp = [[0] * len(bags) for _ in range(len(bags))]
        for d in range(1, len(dp) + 1):
            for l in range(len(dp) - d + 1):
                r = l + d - 1
                if r == l:
                    dp[l][r] = bags[l]
                elif r == l + 1:
                    dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
                else:
                    dp[l][r] = max(
                        bags[l] + min(dp[l + 2][r], dp[l + 1][r - 1]),
                        bags[r] + min(dp[l][r - 2], dp[l + 1][r - 1]),
                    )
        return dp[0][len(bags) - 1]
                
        
        


"""
Zero Sum Games: Bags of gold, we can only take a bag on the left or right, then the opponent's move
5   10     6    2

Interview tips:
1. Play the game
2. Start with the smallest game, make it bigger

Goal of the game: 
	Does the player who goes first win
	Does the second player get more gold?
	How much does the second player gets? (Answer this one then all other can be answered)
	
Observation: Keeping track of my gold or my opponent gold is not necessary
	-> If I know my score, I also knows my opponent's score
	-> Our score only changes every other move
	-> We maximize our score, opponent maximizes their score
		--> We maximize our score, opponent minimizes our score

def gold(l, r):
    if l == r:
        return bags[l]
    elif l + 1 == r: # Two bags left
        return max(bags[l], bags[r])
    else: # More than two bags left
        return max(
            bags[l] + min(gold(l + 2, r), gold(l + 1, r - 1)),
            bags[r] + min(gold(l + 1, r - 1), gold(l, r - 2))
        )
"""
