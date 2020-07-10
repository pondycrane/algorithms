import collections
from typing import List

import base.solution


"""
Get from start word to stop word using the given words. If no path, return ['-1']
"""
class Solution(base.solution.Solution):
    def string_transformation_using_given_dictionary_of_words(self, words: List[str], start: str, stop: str):
            words = list(set([start] + words + [stop]))
            g = collections.defaultdict(list)
            for w in words:
                for i in range(len(w)):
                    g[f'{w[:i]}*{w[i + 1:]}'].append(w)
            
            visited = set()
            if start != stop:
                visited.add(start)
            q = collections.deque([start])
            parents = collections.defaultdict(lambda: None)
            found = False
            while q:
                v = q.popleft()
                for i in range(len(v)):
                    node = f'{v[:i]}*{v[i + 1:]}'
                    for nv in g[node]:
                        if nv not in visited and nv != v:
                            visited.add(nv)
                            parents[nv] = v
                            if nv == stop:
                                found = True
                                break
                            q.append(nv)
                    if found: break
                if found: break
            
            if not found:
                return ['-1']
            res = [nv]
            while parents[nv] != start:
                nv = parents[nv]
                res.append(nv)
            res.append(start)
            res.reverse()
            return res
