class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def bisearch(self, A, left, right, target):
        if left > right:
            return left
        mid = (left + right) / 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.bisearch(A, mid + 1, right, target)
        else:
            return self.bisearch(A, left, mid - 1, target)
            
    def searchInsert(self, A, target):
        return self.bisearch(A, 0, len(A) - 1,  target)
