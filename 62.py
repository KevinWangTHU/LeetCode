class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
s=Solution()
print s.uniquePaths(3,7)
