class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        s, t, j = 0, 0, -1
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            t += gas[i] - cost[i]
            if s < 0:
                j = i
                s = 0
        if t >= 0:
            return j + 1
        else:
            return -1
