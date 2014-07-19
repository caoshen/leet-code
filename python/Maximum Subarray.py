class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        ret, cur = -1e10, 0
        for i in A:
            cur = max(cur + i, i)
            ret = max(ret, cur)
        return ret
        