class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def solve(num, s):
            s += num,
            for i in range(10):
                next = num * 10 + i
                if next > n:
                    break
                solve(next, s)
        s = []
        for i in range(1, min(n, 9)+1):
            solve(i, s)
        return s
s=Solution()
print len(s.lexicalOrder(49999))
