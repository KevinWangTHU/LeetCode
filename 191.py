class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans
s=Solution()
print s.hammingWeight(8)
