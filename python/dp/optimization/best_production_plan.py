import collections
from typing import List

import base.solution


class Solution(base.solution.Solution):
    """
    T: O(N)
    S: O(N)
    """
    def best_production_plan(self, forecast: List[List[int]]) -> int:
        # Overriding the input values are frawned upon
        a = forecast[0][:]
        b = forecast[1][:]

        for i in range(1, len(forecast[0])):
            a[i] = max(a[i - 1], b[i - 2] if i - 2 >= 0 else 0) + a[i]
            b[i] = max(b[i - 1], a[i - 2] if i - 2 >= 0 else 0) + b[i]
        
        return max(a[-1], b[-1])


"""
#9 Best Production Plan
Two products: A & B, one machine can only produce A or B on any day
Goal: maximize profit
Re-configuring machine (A -> B, B -> A) takes a day
Given Forecast, e.g.

a: 6, 2, 4
b: 1, 3, 7

Solution:
day1: A (profit 6)
day2: A -> B (profit 0)
day3: B (profit 7)
total profit: 13
"""
