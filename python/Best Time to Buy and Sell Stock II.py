class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        ret = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ret += prices[i] - prices[i - 1]
        return ret