class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num&0xAAAAAAAA == 0 and num & (num-1) == 0
