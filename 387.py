class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0] * 26
        for c in s:
            d[ord(c)-97] += 1
        for i in range(len(s)):
            if d[ord(s[i]) - 97] == 1:
                return i
        return -1
s=Solution()
print s.firstUniqChar("loveleetcode")
