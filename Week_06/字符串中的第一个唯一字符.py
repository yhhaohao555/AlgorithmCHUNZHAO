class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec = {}
        for c in s:
            rec[c] = rec.setdefault(c, 0) + 1
        for i in range(len(s)):
            if rec[s[i]] == 1:
                return i
        return -1