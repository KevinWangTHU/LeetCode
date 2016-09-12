class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [1] * (n/2)
        count = 1
        for i in range(n/2-1):
            if d[i]:
                count += 1
                prime = i * 2 + 3
                for j in range(prime, n/prime+1, 2):
                    d[(prime*j)/2-1] = 0
        return count if n > 2 else 0

s = Solution()
print s.countPrimes(2)
