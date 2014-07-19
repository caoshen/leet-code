class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 1:
            return 1
        return self.numTrees(n - 1) * ( 4 * n - 2) / (n + 1)