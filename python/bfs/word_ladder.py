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
        