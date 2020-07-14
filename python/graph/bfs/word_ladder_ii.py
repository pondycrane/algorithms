import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    def word_ladder_ii(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g = collections.defaultdict(list)
        wordList.append(beginWord)
        wordList = list(set(wordList))
        for word in wordList:
            for i in range(len(word)):
                g[f'{word[:i]}*{word[i + 1:]}'].append(word)

        q = collections.deque([beginWord])
        parents = collections.defaultdict(list) # Allow multiple parents
        visited = set([beginWord])
        found = False
        while q:
            if found:
                break
            l = len(q)
            batch = set() # Record visited in a batch fashion to allow multiple parents
            for _ in range(l):
                v = q.popleft()
                for i in range(len(v)):
                    for nv in g[f'{v[:i]}*{v[i + 1:]}']:
                        if nv in visited or nv == v:
                            continue
                        parents[nv].append(v)
                        if nv in batch:
                            continue
                        if nv == endWord:
                            found = True
                        batch.add(nv)
                        q.append(nv)
            visited = batch | visited
        if not found: return []
        
        res = []
        def reconstitute(cur):
            lw = cur[-1]
            if not parents[lw]:
                res.append(list(reversed(cur)))
                return
            for w in parents[lw]:
                cur.append(w)
                reconstitute(cur)
                cur.pop()
        reconstitute([endWord])
        return res


"""
126. Word Ladder II
Hard

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
