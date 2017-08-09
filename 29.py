# Trick: Use *2 method.
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == -2**31 and divisor == -1):
            return 2**31-1
        ans = 0
        if dividend * divisor >= 0:
            flag = 1
        else:
            flag = -1

        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            sub = divisor
            count = 1
            while dividend >= sub+sub:
                sub += sub
                count += count
            dividend -= sub
            ans += count

        return ans * flag
