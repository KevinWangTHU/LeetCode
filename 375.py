class Solution(object):
    def getMoneyAmount_WRONG(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n+1)
        f[2] = 1
        g = [0] * (n+1)
        g[2] = 1
        for i in range(3, n+1):
            minF = 999999
            minG = 999999
            for j in range(2, i):
                cost = j + max(f[j-1], f[i-j] + g[i-j]*j)
                time = 1 + max(g[j-1], g[i-j])
                if cost < minF:
                    minF = cost
                    minG = time
            f[i] = minF
            g[i] = minG
        return f[n]

    def getMoneyAmount(self, n):
        f = [[0] * (n+1) for i in range(n+1)]
        for k in range(1, n):
            for i in range(1, n-k+1):
                j = i + k
                MIN = 9999999
                for t in range(i, j):
                    if MIN > t + max(f[i][t-1], f[t+1][j]):
                        MIN = t + max(f[i][t-1], f[t+1][j])
                f[i][j] = MIN
        return f[1][n]
s = Solution()
print s.getMoneyAmount(100)
