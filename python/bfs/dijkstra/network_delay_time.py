import heapq
import typing

import base.solution

class Node:
    def __init__(self, n_id):
        self.n_id = n_id
        self.cost = float('inf')
        self.targets = []

    def __lt__(self, other):
        return self.cost < other.cost

class Solution(base.solution.Solution):
    def network_delay_time(self, times: typing.List[typing.List[int]], N: int, K: int) -> int:
        graph = {i: Node(i) for i in range(1, N + 1)}
        seen = set()
        for source, target, cost in times:
            graph[source].targets.append((target, cost))
        
        graph[K].cost = 0
        h = [graph[K]]
        while h:
            node = heapq.heappop(h)
            seen.add(node.n_id)
            if len(seen) == N:
                break
            
            for target, cost in node.targets:
                next_n = graph[target]
                if node.cost + cost < next_n.cost:
                    next_n.cost = node.cost + cost
                    if next_n.n_id != K:
                        heapq.heappush(h, next_n)
        
        return node.cost if len(seen) == N else -1
            


"""
743. There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""