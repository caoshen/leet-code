class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        max_pos = 0
        for i in range(len(A)):
            if max_pos < i:
                return False
            elif max_pos >= len(A) - 1:
                return True
            max_pos = max(max_pos, i + A[i])
        return True