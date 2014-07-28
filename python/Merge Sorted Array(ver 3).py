class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        while m and n:
            if A[m - 1] < B[n - 1]:
                A[m + n - 1] = B[n - 1]
                n -= 1
            else:
                A[m + n - 1] = A[m - 1]
                m -= 1
        if m == 0:
            A[: m + n] = B[: n]