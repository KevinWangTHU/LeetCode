import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # So the problem is: how many 5s are in 1-n
        return sum([n/5**k for k in range(1, int(math.log(n, 5))+1)])


s = Solution()
print s.trailingZeroes(1000)
