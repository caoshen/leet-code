class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        f = [0] * 10000
        f[0], f[1] = 1, 1
        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    f[i] = f[i - 2]
                else:
                    f[i] = 0
            else:
                if s[i - 2] == '1' or s[i -2] == '2' and s[i - 1] <= '6':
                    f[i] = f[i - 1] + f[i - 2]
                else:
                    f[i] = f[i - 1]
        return f[len(s)]