class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursion(nums, temp):
            if not nums:
                ans.append(temp)
                return
            for i in range(len(nums)):
                recursion(nums[:i] + nums[i + 1:], temp + [nums[i]])
        
        ans = []
        recursion(nums, [])
        return ans