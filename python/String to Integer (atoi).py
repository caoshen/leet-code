class Solution:
    # @return an integer
    def atoi(self, str):
        result = 0
        length , sign, i = len(str), 1, 0
        if length == 0:
            return result
        while  i < length and str[i] == ' ' :
            i += 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1
        
        for s in str[i:]:
            if s < '0' or s > '9':
                break
            result = result * 10 + int(s)
        result *= sign
        if result >= 2147483648:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result
