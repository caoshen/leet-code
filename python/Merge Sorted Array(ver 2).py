class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        ret = []
        i, j = 0, 0
        while i < m and j < n:
            if A[i] < B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        if i == m:
            ret.extend(B[j:])
        else:
            ret.extend(A[i:])
        A[:] = ret