class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        count = 0xFFFFFFFF
        while count != 0:
            ans <<= 1
            digit = n & 1
            ans |= digit
            n >>= 1
            count >>= 1

        return ans

s=Solution()
s.reverseBits(43261596)
