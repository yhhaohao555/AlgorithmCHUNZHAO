class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1
        for c in t:
            if c in dic.keys():
                dic[c] -= 1
                if dic[c] < 0:
                    return False
            else:
                return False
        return True