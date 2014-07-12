class Solution {
public:
    int searchInsert(int A[], int n, int target) {
        return bisearch(A, 0, n - 1, target);
    }
    int bisearch(int A[], int left, int right, int target) {
        if (left  > right)
            return left;
        int mid = (left + right) >> 1;
        if (A[mid] == target)
            return mid;
        else if (A[mid] < target)
            return bisearch(A, mid + 1, right, target);
        else
            return bisearch(A, left, mid - 1, target);
    }
};