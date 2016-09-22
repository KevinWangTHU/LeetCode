class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        count = 9
        while n > count * digit:
            n -= count * digit
            count *= 10
            digit += 1
        num = 10**(digit-1) + (n-1)/digit
        pos = (n-1) % digit
        return str(num)[pos]


s=Solution()
print s.findNthDigit(333333)
