class Solution(object):
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if i == j:
                    dp[i][j] = True
                    count += 1
                    continue
                if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                    count += 1
        return count