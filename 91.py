class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0":
            return 0
        f = [1]
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] == "0" or s[i-1] > "2":
                    return 0
                f.append(f[i-2])
            else:
                f.append(f[i-1] + (f[i-2] if "10" < s[i-1:i+1] <= "26" else 0))
        return f[-1]
s = Solution()
print s.numDecodings("1223")
