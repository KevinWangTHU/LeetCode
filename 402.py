class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s = []
        for i in range(len(num)):
            while s and s[-1] > num[i] and k > 0:
                s.pop()
                k -= 1
            s.append(num[i])
        while k > 0 and s:
            s.pop()
            k -= 1
        for i in range(len(s)):
            if s[i] != "0":
                break
        return "".join(s[i:]) or "0"
s=Solution()
print s.removeKdigits("1432219",3)
