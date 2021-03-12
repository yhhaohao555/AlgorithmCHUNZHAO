学习笔记
分并排序：
def merge(self, left_nums, right_nums):
        cur = 0
        left = 0
        right = 0
        answer = []
        for i in range(len(left_nums) + len(right_nums)):
            if left >= len(left_nums):
                answer.append(right_nums[right])
                right += 1
            elif right >= len(right_nums):
                answer.append(left_nums[left])
                left += 1
            else:
                if left_nums[left] > right_nums[right]:
                    answer.append(right_nums[right])
                    right += 1
                else:
                    answer.append(left_nums[left])
                    left += 1
        return answer
    
    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left_nums = self.merge_sort(nums[0: mid])
        right_nums = self.merge_sort(nums[mid: len(nums)])
        answer = self.merge(left_nums, right_nums)
        return answer

快速排序：
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        shuffle(nums)
        self.quickSort(nums, 0, len(nums)-1)
        # nums.sort()
        return nums[-k]


    def quickSort(self, nums, left, right):
        if left >= right:
            return
        pivot = nums[left]
        i = left
        j = right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] < pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        
        self.quickSort(nums, left, i-1)
        self.quickSort(nums, i+1, right)

不同路径2状态转移方程：
if grid[i][j] is stone:
	dp[i][j] = 0
else:
	dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
