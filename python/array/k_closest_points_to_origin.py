import collections
import random
import typing

import base.solution

class Solution(base.solution.Solution):
    def k_closest_points_to_origin(self, points: typing.List[int], K: int) -> int:
        if not points or K > len(points) or K <= 0:
            raise ValueError('Invalid input')
        
        def eucdistance(x, y):
            return (x**2 + y**2)**0.5

        eudis = [(eucdistance(x, y), i) for i, (x, y) in enumerate(points)]
        queue = collections.deque()
        queue.append((0, len(eudis) - 1))
        result = []
        while queue:
            start, end = queue.pop()
            if start > end:
                continue
            
            pivot = random.randint(start, end)
            eudis[start], eudis[pivot] = eudis[pivot], eudis[start]
            pivot = i = start
            j = i + 1
            while j <= end:
                if eudis[j][0] <= eudis[pivot][0]:
                    i += 1
                    eudis[i], eudis[j] = eudis[j], eudis[i]
                j += 1
            eudis[i], eudis[pivot] = eudis[pivot], eudis[i]
            if i >= K:
                queue.append((start, i - 1))
            else:
                result.append(points[eudis[i][1]])
                queue.append((i + 1, end))
                queue.append((start, i - 1))
        return result


"""
973. K Closest Points to Origin
Medium

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""