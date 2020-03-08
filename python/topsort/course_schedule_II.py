import collections
import typing

import base.solution

class Solution(base.solution.Solution):
    def course_schedule_II(self, dependencies: typing.List[typing.List[int]] = []):
        if type(dependencies) is not list:
            raise TypeError(f"Input type error {type(dependencies)}")
        
        graph = collections.defaultdict(set)
        visit = collections.defaultdict(int)
        # Use visit dict to track status
        # 0: unvisited; 1: visiting; 2: visited
        for a, b in dependencies:
            graph[b].add(a)
            graph[a]
            visit[a]
            visit[b]
        
        def is_cycle(course):
            visit[course] = 1
            for next_course in graph[course]:
                if visit[next_course] == 1:
                    return True
                if not visit[next_course] and is_cycle(next_course):
                    return True
            res.append(course)
            visit[course] = 2
            return False

        res = []
        for course in graph:
            if not visit[course] and is_cycle(course):
                return []

        return res[::-1]
"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""