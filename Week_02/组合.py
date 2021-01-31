class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def recursion(cur, comb):
            if len(comb) == k:
                ans.append(comb)
                return
            for i in range(cur, n + 1):
                recursion(i + 1, comb + [i])
        
        ans = []
        recursion(1, [])
        return ans