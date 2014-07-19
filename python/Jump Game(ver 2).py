class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reach, i = 1, 0
        while i < reach and reach < len(A):
            reach = max(reach, 1 + i + A[i])
            i += 1
        return reach >= len(A)