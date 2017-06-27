from math import sqrt, ceil
class Solution(object):
    def numSquares_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0]
        for i in xrange(1, n+1):
            m = 999999
            for j in xrange(1, int(ceil(sqrt(i)))+1):
                m = min(m, f[i - j*j])
            f.append(m + 1)
        return f[n]

    def numSquares_2(self, n):
        f = [0] + [99999] * n
        q = [0]
        length = 0
        while q:
            nextq = []
            length += 1
            while q:
                num = q.pop()
                for i in range(1, n+1):
                    if num + i*i > n:
                        break
                    if num + i*i == n:
                        return length
                    if f[num + i*i] == 99999:
                        f[num + i*i] = length
                        nextq.append(num + i*i)
            q = nextq

    def numSquares(self, n):
        s, t = {0}, {n}
        vis = [True] + [False] * (n-1) + [True]
        def search(cur, other, forward, length):
            if len(cur) > len(other):
                return search(other, cur, -forward, length)
            next = set()
            for num in cur:
                for i in range(1, n+1):
                    t = num + i*i*forward
                    if t > n or t < 1:
                        break
                    if t in other:
                        return length
                    if not vis[t]:
                        vis[t] = True
                        next.add(t)
            return search(next, other, forward, length+1)
        return search(s, t, 1, 1)

s = Solution()
print s.numSquares(99999)
