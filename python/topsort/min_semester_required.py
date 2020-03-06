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
    def min_semester_required(self, dependencies: List[List[int]] = []):
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
        
        course_schedule = []
        def dfs(node, semester):
            for prerequisite in node.children:
                print(total_courses)
                if graph[prerequisite] in total_courses:
                    graph[prerequisite].incoming_count -= 1
                    dfs(graph[prerequisite], semester + 1)

            if node.incoming_count == 0:
                while len(course_schedule) - 1 < semester:
                    course_schedule.append([])
                course_schedule[semester].append(node.val)
                total_courses.remove(node)
                        
        for node in [n for n in graph.values() if n.incoming_count == 0]:
            dfs(node, 0)

        if len(total_courses) > 0:
            return None

        return course_schedule