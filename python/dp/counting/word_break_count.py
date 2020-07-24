import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    Got timeout and wrong answer
    """
    def word_break_count(self, dictionary: List[str], txt: str) -> int:
        validdic = [w for w in dictionary if w in txt]
        dp = [0] * (len(txt) + 1)
        for i in range(len(dp)):
            for w in validdic: # inefficient iteration of words and substring copying
                if i - len(w) < 0:
                    continue
                if txt[i - len(w): i] == w:
                    if i - len(w) == 0:
                        dp[i] += 1
                    dp[i] += dp[i - len(w)]
        return dp[len(txt)]


    """
    More efficient way. Cache the word length and save the words in hashset for fast checking.
    """
    def word_break_count(self, dictionary: List[str], txt: str) -> int:
        words = set(dictionary)
        lengths = set([len(w) for w in words])
        dp = [0] * (len(txt) + 1)
        for i in range(1, len(dp)):
            for l in lengths:
                if i - l == 0 and txt[i - l: i] in words:
                    dp[i] += 1
                elif i - l > 0 and txt[i - l: i] in words:
                    dp[i] += dp[i - l]
        return dp[len(txt)] % (10 ** 9 + 7)



"""
Find how many ways a given word can be broken into the pieces provided in dictionary
"""

