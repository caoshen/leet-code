class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], c = (digits[i] + c) % 10, (digits[i] + c) / 10
        if c != 0:
            digits = [c] + digits
        return digits
