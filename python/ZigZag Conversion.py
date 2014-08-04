class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1 or len(s) == 1:
            return s
        v_index , v = 0, [''] * nRows
        for i in range(len(s)):
            x = i % (2 * nRows - 2)
            if x <= nRows - 1:
                v_index = x
            else:
                v_index = 2 * nRows - 2 - x
            v[v_index] += s[i]
        return ''.join(v)