class Solution:
    # @return a string
    def longestPalindrome(self, s):
        str = '^#' + '#'.join(s) + '#$'
        mx, id = 0, 0
        p = [0] * len(str)
        for i in range(1, len(str) - 1):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1
            while  str[i - p[i]] == str[i + p[i]]:
                p[i] += 1
            if mx < i + p[i]:
                mx = i + p[i]
                id = i
        maxlen = max(p[1 : len(str) - 1]);
        pos = p.index(maxlen)
        start = (pos  - maxlen) / 2
        end = (pos + maxlen) / 2 - 1
        return s[start: end]
        
