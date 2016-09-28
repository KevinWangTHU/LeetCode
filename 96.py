class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1]
        for i in range(1, n+1):
            s = 0
            for j in range(i):
                s += f[j] * f[i-j-1]
            f.append(s)
        return f[-1]
s=Solution()
print s.numTrees(3)
