import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def group_anagrams(self, strs: typing.List[str]) -> typing.List[typing.List[str]]:
        res = collections.defaultdict(list)
        for word in strs:
            res[''.join(sorted(word))].append(word)
        
        return list(res.values())

    def group_anagrams(self, strs: typing.List[str]) -> typing.List[typing.List[str]]:
        res = collections.defaultdict(list)
        def build_key(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            return ','.join(map(str, count))
        
        for word in strs:
            res[build_key(word)].append(word)
        return list(res.values())

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""