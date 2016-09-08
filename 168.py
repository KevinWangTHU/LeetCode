class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = []
        while n > 0:
            remain = (n-1) % 26
            ans.append(chr(remain+65))
            n = (n-1)/26

        return "".join(reversed(ans))
