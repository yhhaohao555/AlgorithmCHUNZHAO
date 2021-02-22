class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        dp[1] = ["()"]
        for i in range(2, n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - 1 - j]:
                        dp[i].append('(' + x + ')' + y)
        return dp[n]