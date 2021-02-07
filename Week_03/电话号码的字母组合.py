class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = { 
                '2': ['a', 'b', 'c'], 
                '3': ['d', 'e', 'f'], 
                '4': ['g', 'h', 'i'], 
                '5': ['j', 'k', 'l'], 
                '6': ['m', 'n', 'o'], 
                '7': ['p', 'q', 'r', 's'], 
                '8': ['t', 'u', 'v'], 
                '9': ['w', 'x', 'y', 'z']
              }
        ans = []
        def recur(index, s):
            if index == len(digits):
                ans.append(s)
                return
            for c in dic[digits[index]]:
                recur(index + 1, s + c)
        if not digits:
            return ans
        recur(0, "")  
        return ans