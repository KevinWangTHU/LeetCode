class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        t = m
        base = 1
        while t:
            t /= 2
            base *= 2
        if n > base:
            return 0
        t = m ^ n
        mask = 0x7FFFFFFF
        while t:
            t >>= 1
            mask <<= 1
        return m & mask
