class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        H, L, R = [0] * n, [0] * n, [n] * n
        result = 0
        for i in range(m):
            left, right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    left = j + 1
                    L[j] , R[j], H[j] = 0, n, 0
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j
        return result