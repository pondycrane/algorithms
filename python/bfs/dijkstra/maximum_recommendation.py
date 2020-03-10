import base.solution
import collections
import heapq
import typing

"Given a list of recommendations [a, b] = a recommends b, return the minimum clicks starting from 0"
"required to achieve maximum recommendation"

class Page:
    def __init__(self, page_id):
        self.page_id = page_id
        self.cost = float('inf')
        self.recommendations = []
        self.visited = False

    def __lt__(self, other):
        return self.cost < other.cost

class Solution(base.solution.Solution):
    def maximum_recommendation(self, recommends: typing.List[int]) -> int:
        recommends.sort()
        graph = {}
        max_node = None
        max_r_count = float('-inf')
        for a, b in recommends:
            for p in [a, b]:
                if p not in graph:
                    graph[p] = Page(p)
            graph[a].recommendations.append(b)
            if len(graph[a].recommendations) > max_r_count:
                max_node = graph[a]
        graph[0].cost = 0
        h = [graph[0]]
        while h:
            node = heapq.heappop(h)
            node.visited = True
            for next_n_key in node.recommendations:
                next_n = graph[next_n_key]
                next_n.cost = min(next_n.cost, node.cost + 1)
                if next_n != max_node.page_id and not next_n.visited:
                    heapq.heappush(h, next_n)
        return max_node.cost


