class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        maxLen = 0
        ans = (0, 0)
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = 2
                    elif dp[i + 1][j - 1] > -1:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    ans = (i, j)
        return s[ans[0]: ans[1] + 1]