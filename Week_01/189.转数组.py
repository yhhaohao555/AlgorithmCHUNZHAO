class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        k = k % (n + 1)
        self.reverse(nums, 0, n)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1