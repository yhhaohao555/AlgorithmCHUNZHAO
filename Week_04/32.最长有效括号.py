class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i > 1 else 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                res = max(res, dp[i])
        return res