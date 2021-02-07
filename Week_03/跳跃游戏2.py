class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxIndex = 0
        step = 0
        tmpIndex = 0
        for i in range(len(nums) - 1):
            if tmpIndex >= i and i + nums[i] > tmpIndex:
                tmpIndex = i + nums[i]
            if i == maxIndex:
                maxIndex = tmpIndex
                step += 1
        return step