class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        s = []
        mr , i = 0, 0
        while i < len(height):
            if len(s) == 0 or height[i] > height[s[-1]]:
                s.append(i)
                i += 1
            else:
                h = height[s.pop()]
                l = 0
                if len(s) == 0:
                    l = i
                else:
                    l = i - s[-1] - 1
                mr = max(mr, h * l)
        return mr
            
