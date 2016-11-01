class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = [0] * len(s)
        even = [-1] * len(s)
        for i in range(1, len(s)):
            for j in range(min(i+1, len(s)-i)):
                if s[i-j] != s[i+j]:
                    break
                odd[i] = j
            for j in range(min(i, len(s)-i)):
                if s[i-j-1] != s[i+j]:
                    break
                even[i] = j

        def ispal(i, j):
            return odd[(i+j)/2] >= (j-i)/2 if (j-i) % 2 == 0 else even[(i+j+1)/2] >= (j-i)/2

        f = [-1] + [9999999] * len(s)
        for j in range(1, len(s)+1):
            for i in range(1, j+1):
                if ispal(i-1, j-1):
                    f[j] = min(f[j], f[i-1]+1)
        return f[-1]
s=Solution()
print s.minCut("aab")
