class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n > 0 and 1162261467 % n == 0 else False
