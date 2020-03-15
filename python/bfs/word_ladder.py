import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def word_ladder(self, beginWord: str, endWord: str, wordList: typing.List[str]) -> int:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(bool)
        for word in wordList + [beginWord]:
            visited[word]
            for i in range(len(word)):
                graph[word[0:i] + '*' + word[i + 1:]].append(word)

        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, cost = queue.popleft()
            visited[word] = True
            for i in range(len(word)):
                key = word[0:i] + '*' + word[i + 1:]
                for n_word in graph[key]:
                    if n_word == endWord:
                        return cost + 1
                    
                    if n_word != word and not visited[n_word]:
                        queue.append((n_word, cost + 1))
                graph[key] = []
        return 0

"""
127. Word Ladder
Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""