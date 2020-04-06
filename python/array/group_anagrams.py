import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def group_anagrams(self, strs: typing.List[str]) -> typing.List[typing.List[str]]:
        res = collections.defaultdict(list)
        for word in strs:
            res[str(collections.Counter(sorted(word)))].append(word)
        
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