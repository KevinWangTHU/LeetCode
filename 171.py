class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        pow = 1
        ans = 0
        for c in reversed(s):
            num = (ord(c) - 64) * pow
            pow *= 26
            ans += num
        return ans

s = Solution()
print s.titleToNumber("AAA")
