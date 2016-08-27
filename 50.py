class Solution(object):
    def myPow_slow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ret = 1.0
        if n < 0: # Caution!
            n = -n
            x = 1/x
        while n:
            tmp = x
            power = 1
            while n > 2*power:
                power *= 2
                tmp *= tmp
            n -= power
            ret *= tmp

        return ret

    def myPow_fast(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            if n & 1:
                pow *= x
            n /= 2
            x *= x
        return pow
