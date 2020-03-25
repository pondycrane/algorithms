import collections
import enum
import typing

import base.solution
import lib.ds_collections.treenode as treenode

class State(enum.Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

class Solution(base.solution.Solution):

    def g_4_7_build_order(self, dependencies: typing.List[typing.List[int]]) -> typing.List[int]:
        graph = collections.defaultdict(list)
        visit = collections.defaultdict(lambda : State.UNVISITED)
        for a, b in dependencies:
            graph[a].append(b)
            visit[a]
            visit[b]
        
        def traverse(node):
            visit[node] = State.VISITING
            for next_n in graph[node]:
                if visit[next_n] == State.VISITING:
                    raise ValueError(f"{dependencies} does not have valid order")
                if visit[next_n] == State.UNVISITED:
                    traverse(next_n)
            visit[node] = State.VISITED
            order.append(node)

        order = []
        for node in visit:
            if visit[node] == State.UNVISITED:
                traverse(node)
        
        return order[::-1]


"""
4.7 Build Order: You are given a list of projects and a list of
dependencies (which is a list of pairs of projects where the second
project is dependent on the first project). All of a project's dependencies
must be build before the the project is. Find a build order that will allow
the projects to be built. If there is no valid build order, return an error.

EXAMPLE
input:
  projects: a, b, c, d, e, f
  dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

Output: f, e, a, b, d, c
"""