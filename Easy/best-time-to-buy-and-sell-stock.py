from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_val = prices[0]
        profit = 0
        for val in prices[1:]:
            if val < curr_val:
                curr_val = val
                continue
            if profit < val - curr_val:
                profit = val - curr_val

        return profit
