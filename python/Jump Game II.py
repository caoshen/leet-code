class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        max_pos, last_pos, ret = 0, 0, 0
        for i in range(len(A)):
            if i > last_pos:
                last_pos = max_pos
                ret += 1
                if last_pos >= len(A) - 1:
                    return ret
            max_pos = max(max_pos, i + A[i])
        return ret