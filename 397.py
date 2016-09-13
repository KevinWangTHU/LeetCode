class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n/2) + 1
        else:
            return min(self.integerReplacement(n/2),
                       self.integerReplacement(n/2+1)) + 2
s=Solution()
print s.integerReplacement(1000133000)
