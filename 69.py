class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ym = 1.0
        while True:
            y = ym - (ym**2-x)/(2*ym)
            if abs(y-ym) < 1e-3:
                break
            ym = y

        return int(y)
