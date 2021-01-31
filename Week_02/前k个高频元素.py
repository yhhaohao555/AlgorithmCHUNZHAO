class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        hp = []
        heapq.heapify(hp)
        for x in nums:
            dic[x] = dic.setdefault(x, 0) + 1
        for key in dic.keys():
            if len(hp) < k:
                heapq.heappush(hp, (dic[key], key))
            elif hp[0][0] <= dic[key]:
                heapq.heappush(hp, (dic[key], key))
                heapq.heappop(hp)
        ans = [x[1] for x in hp]
        return ans