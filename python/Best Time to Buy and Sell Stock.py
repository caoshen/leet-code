class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        ret , minp = 0, 1e20 
        for i in prices:
            minp = min(minp, i)
            ret = max(ret, i - minp)
        return ret
            