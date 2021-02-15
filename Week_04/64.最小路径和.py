class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = grid[:]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]