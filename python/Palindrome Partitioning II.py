class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        f = [0] * (n + 1)
        p = [[False] * n for i in range(n)]
        for i in range(n + 1):
            f[i] = n - 1 - i
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1] == True):
                    p[i][j] = True
                    f[i] = min(1 + f[j + 1], f[i])
        return f[0]