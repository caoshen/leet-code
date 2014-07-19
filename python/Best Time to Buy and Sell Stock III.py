class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        left, right = [], []
        mp, mi, mm = 0, prices[0], prices[-1]
        for i in prices:
            mi = min(mi, i)
            mp = max(mp, i - mi)
            left.append(mp)
        mp = 0
        for i in prices[ : : -1]:
            mm = max(mm, i)
            mp = max(mp, mm - i)
            right.append(mp)
        ret = 0
        for i in range(len(prices)):
            ret = max(ret, left[i] + right[len(prices) - i - 1])
        return ret