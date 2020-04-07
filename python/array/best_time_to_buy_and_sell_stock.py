import functools
import typing

import base.solution

class Solution(base.solution.Solution):
    def best_time_to_buy_and_sell_stock(self, prices: typing.List[int]) -> int:
        if not prices:
            return 0
            
        return functools.reduce(
            lambda a, b: (
                min(a[0], b),
                max(a[1], b - min(a[0], b))
            ),
            prices,
            (float('inf'), float('-inf'))
        )[1]