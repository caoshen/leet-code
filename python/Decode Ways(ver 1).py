class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        a, b = 1, 0
        for i in range(len(s)):
            if s[i] == '0':
                a = 0
            if i >= 1 and not (s[i -1] == '1' or s[i - 1] == '2' and s[i] in '0123456'):
                b = 0
            t = a
            a = a + b
            b = t
        return a