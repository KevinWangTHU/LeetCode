class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        cut = []
        for i in range(len(s)):
            if s[i] in ["I", "X", "C"] and i < len(s)-1 and d[s[i+1]] > d[s[i]]:
                cut.append(-d[s[i]])
            else:
                cut.append(d[s[i]])
        # print cut
        return sum(cut)

s = Solution()
print s.romanToInt("XXXIX")
