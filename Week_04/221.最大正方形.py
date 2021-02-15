class Solution(object):
    def maximalSquare(self, matrix):
        res = 0
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res * res