# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: ms: beats %
# Memory: MB: beats %
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        max_price = 0
        profit = 0
        for i in prices:
            if min_price > i:
                min_price = i
                max_price = i
            if max_price < i:
                max_price = i
            profit = max_price - min_price if profit < max_price - min_price else profit
        return profit


if __name__ == '__main__':
    ps = [7, 4, 10, 5, 1, 5]
    print(Solution().maxProfit(ps))
