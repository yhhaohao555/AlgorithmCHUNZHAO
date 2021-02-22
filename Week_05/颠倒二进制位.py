class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res += (n & 1) << (31 - i)
            n = n >> 1
        return res