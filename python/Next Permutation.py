class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        partition = -1
        for i in range(len(num) - 2, - 1, -1):
            if num[i] < num[i + 1]:
                partition = i
                break
        if partition == -1:
            return num[::-1]
        for i in range(len(num) - 1, partition, -1):
            if num[i] > num[partition]:
                num[i], num[partition] = num[partition], num[i]
                break
        return num[:partition + 1] + num[:partition:-1]
        