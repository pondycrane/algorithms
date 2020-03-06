import collections
from typing import List

import base.solution

class GNode:
    def __init__(self, val):
        self.val = val
        self.incoming_count = 0
        self.children = []

"""
You are given a list of course dependencies, find the courses need to take.
Input: list of dependences. [a, b] means class a depends on finishing class b.
"""
class Solution(base.solution.Solution):
    def course_schedule(self, dependencies: List[List[int]] = []):
        if type(dependencies) is not list:
            raise TypeError(f"Input type error {type(dependencies)}")

        graph = collections.defaultdict(GNode)

        total_courses = set()
        for c, pre in dependencies:
            if pre not in graph:
                graph[pre] = GNode(pre)
            if c not in graph:
                graph[c] = GNode(c)
            pre_node = graph[pre]
            c_node = graph[c]
            pre_node.children.append(c)
            c_node.incoming_count += 1
            total_courses.add(pre_node)
            total_courses.add(c_node)
        
        queue = collections.deque([(n, 0) for n in graph.values() if n.incoming_count == 0])
        course_schedule = []
        while queue:
            node, semester = queue.popleft()
            
            for prerequisite in node.children:
                next_node = graph[prerequisite]
                next_node.incoming_count -= 1
                if next_node.incoming_count == 0:
                    queue.append((next_node, semester + 1))

            if node.incoming_count == 0:
                while len(course_schedule) - 1 < semester:
                    course_schedule.append([])
                course_schedule[semester].append(node.val)
                total_courses.remove(node)

        if len(total_courses) > 0:
            return None

        return course_schedule