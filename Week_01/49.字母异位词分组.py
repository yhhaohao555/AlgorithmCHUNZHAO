class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans_dict = {}
        for s in strs:
            # print(self.hashcode(s))
            code = self.hashcode(s)
            if code in ans_dict.keys():
                ans_dict[code].append(s)
            else:
                ans_dict[code] = [s]
        ans = list(ans_dict.values())

        return ans


    def hashcode(self, s):
        count = {}
        code = ""
        for c in s:
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        for i in sorted(count):
            code += str(i) + str(count[i])
        return code