class Solution(object):
    def countBits(self, num):
        dp = [1 for i in range(num + 1)]
        dp[0] = 0
        for i in range(3, num + 1):
            if i & 1 == 1:
                dp[i] += dp[i - 1]
            else:
                dp[i] = dp[i // 2]
        return dp