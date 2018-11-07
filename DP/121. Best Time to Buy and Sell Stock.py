# coding=utf-8


# DP solution:
# 在这里dp的想法是这样的，dp[i] = [lowest price seen before, maximum profit can get now]
# dp[i][0] = min(dp[i - 1][0], prices[i])
# dp[i][1] = max(prices[i] - dp[i][0], dp[i - 1][1])


# 28ms
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        # DP solution:
        # Use dp to record [lowest price seen before, maximum profit] of each day
        if len(prices) == 0: return 0
        lowest_price = [0] * len(prices)
        max_profit = [0] * len(prices)
        lowest_price[0] = prices[0]
        for i in xrange(1, len(prices)):
            lowest_price[i] = min(lowest_price[i - 1], prices[i])
            max_profit[i] = max(prices[i] - lowest_price[i], max_profit[i - 1])
        return max_profit[len(prices) - 1]

# Non DP solution：24ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        mins, maxs = prices[0], prices[0]
        res = 0
        for price in prices:
            if price > maxs:
                maxs = price
            if price < mins:
                res = max(res, maxs - mins)
                mins = maxs = price
        return max(res, maxs - mins)
