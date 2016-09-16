# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if num == 5:
        return 0
    if num < 5:
        return -1
    else:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = (l+r) / 2
            if guess(m) == -1:
                l = m + 1
            else:
                r = m - 1
        return l

s = Solution()
print s.guessNumber(10)
