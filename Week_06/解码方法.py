class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        def getNum(i):
            return int(s[i - 1] + s[i])
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if i == 0:
                dp[i] = 1
                continue
            if s[i] != '0':
                dp[i] += dp[i - 1]
            num = getNum(i)
            if num >= 10 and num <= 26:
                dp[i] += dp[i - 2] if i > 1 else 1
        return dp[-1]
            