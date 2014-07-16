class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        for i in range(0, len(strs[0])):
            for j in strs[1:]:
                if i < len(j) and strs[0][i] != j[i] or i >= len(j):
                    return strs[0][:i]
        return strs[0]