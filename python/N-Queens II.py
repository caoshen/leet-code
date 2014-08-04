class Solution:
    # @return an integer
    def totalNQueens(self, n):
        ret = 0
        return self.dfs(ret, [], 0, n)
        
    def dfs(self, ret, col, index, n):
        if index == n:
            return ret + 1
        else:
            for i in range(n):
                if i not in col and \
                    all(map (lambda c : abs(col[c] - i) != abs(c - index), range(index))):
                    col.append(i)
                    ret = self.dfs(ret, col, index + 1, n)
                    col.pop()
            return ret
