class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
        int m = matrix.size();
        if (!m)
            return 0;
        int n = matrix[0].size();
        // 分别是第 m 行 第 n 列的点能够扩展（向上，向左，向右）的最大矩形的高，左边界，右边界 + 1
        vector<int> H(n, 0);
        vector<int> L(n, 0);
        vector<int> R(n, n);
        int result = 0;
        for (int i = 0; i < m; ++i) {
            int left = 0, right = n;
            // caculate L(i, j) from left to right
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '1') {
                    ++H[j];
                    L[j] = max(L[j], left);
                }
                else {
                    left = j +  1;
                    H[j] = 0;
                    L[j] = 0;
                    R[j] = n;
                }
            }
            // caculate R[i, j] from right to left
            for (int j = n - 1; j >= 0; --j) {
                if (matrix[i][j] == '1') {
                    R[j] = min(R[j], right);
                    result = max(result, H[j] * (R[j] - L[j]));
                }
                else
                    right = j;
            }
        }
        return result;
    }
};