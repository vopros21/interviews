# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: ms: beats %
# Memory: MB: beats %
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = max(prices[i:]) - min_price if profit < max(prices[i:]) - min_price else profit
        return profit


if __name__ == '__main__':
    ps = [7]
    print(Solution().maxProfit(ps))
