class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        cur = m + n - 1
        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[cur] = nums1[p1]
                cur -= 1
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                cur -= 1
                p2 -= 1
        while p1 > -1:
            nums1[cur] = nums1[p1]
            cur -= 1
            p1 -= 1
        while p2 > -1:
            nums1[cur] = nums2[p2]
            cur -= 1
            p2 -= 1