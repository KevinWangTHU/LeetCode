class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0, 1]
        for i in range(2, n+1):
            Max = i-1
            for j in range(2, i-1):
                if max(i-j, f[i-j]) * j > Max:
                    Max = max(i-j, f[i-j]) * j
            f.append(Max)
        return f[n]


s=Solution()
print s.integerBreak(10)
