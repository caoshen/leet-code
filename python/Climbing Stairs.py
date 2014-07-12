class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a, b = 0, 1
        for i in range(0, n):
            t = b
            b = a + b
            a = t
        return b
