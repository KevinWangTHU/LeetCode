class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pS = pT = 0
        while pS < len(s):
            while pT < len(t) and s[pS] != t[pT]:
                pT += 1
            if pT == len(t):
                return False
            else:
                pS += 1
                pT += 1
        return True
s = Solution()
print s.isSubsequence("abc", "aabbc")
