# coding=utf-8


# DP solution:
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
        dp = [[prices[0], 0]]
        for i in range(1, len(prices)):
            if prices[i] <= dp[i-1][0]:
                dp.append([prices[i], dp[i-1][1]])
            else:
                profit = prices[i] - dp[i-1][0]
                if profit > dp[i-1][1]:
                    dp.append([dp[i-1][0], profit])
                else:
                    dp.append(dp[i-1])
        return dp[-1][1]

# Non DP solution：
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
