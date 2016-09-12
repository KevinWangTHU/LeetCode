class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def digitalize(s):
            d = {}
            count = 0
            ans = []
            for c in s:
                if c not in s:
                    d[c] = count
                    count += 1
                ans.append(d[c])
            return ans
        digitS, digitT = digitalize(s), digitalize(t)
        return True if digitS == digitT else False
