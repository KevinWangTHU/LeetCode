class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"
        mask = 0xFFFFFFFF
        num = num & mask
        ans = []
        while num != 0:
            cur = num & 0xF
            ans.append(chr(cur-10+97) if cur > 9 else str(cur))
            num >>= 4
        return "".join(reversed(ans))
s=Solution()
print s.toHex(1231238)
