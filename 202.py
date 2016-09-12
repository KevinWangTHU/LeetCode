class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getSqrSum(n):
            ans = 0
            while n > 0:
                ans += (n % 10) ** 2
                n /= 10
            return ans
        d = {}
        while True:
            if n == 1:
                return True
            if n in d:
                return False
            d[n] = 1
            n = getSqrSum(n)
s = Solution()
print s.isHappy(19)
