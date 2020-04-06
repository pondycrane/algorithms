import base.solution
import typing

class Solution(base.solution.Solution):
    def best_time_to_buy_and_sell_stock_ii(self, prices: typing.List[int]) -> int:
        if not prices:
            return 0
        
        hold = [float('-inf')] * len(prices)
        clear = [float('-inf')] * len(prices)

        hold[0] = -prices[0]
        clear[0] = 0
        for i in range(1, len(prices)):
            clear[i] = max(hold[i - 1] + prices[i], clear[i - 1])
            hold[i] = max(clear[i - 1] - prices[i], hold[i - 1])
        
        return max(clear[-1], hold[-1])


"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""