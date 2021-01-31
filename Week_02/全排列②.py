class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursion(nums, temp):
            if not nums:
                ans.add(" ".join(temp))
                return
            for i in range(len(nums)):
                recursion(nums[:i] + nums[i + 1:], temp + [str(nums[i])])
        res = []
        ans = set()
        recursion(nums, [])
        for s in list(ans):
            l = s.split()
            for i in range(len(l)):
                l[i] = int(l[i])
            res.append(l)
        return res
