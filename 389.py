class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds, dt = [0] * 26, [0] * 26
        for c in s:
            ds[ord(c)-97] += 1
        for c in t:
            dt[ord(c)-97] += 1
        for i in range(26):
            if ds[i] != dt[i]:
                return chr(i+97)
