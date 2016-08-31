class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        while n > 1:
            a, b = b, a+b
            n -= 1
        return b
