class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bit = [0]
        while len(bit) <= num:
            for i in range(len(bit)):
                bit.append(bit[i]+1)
        return bit[:num+1]
