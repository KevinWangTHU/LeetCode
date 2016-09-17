# Cantor expansion
from math import factorial as factorial
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        ans = []
        while n > 0:
            ans.append(k/factorial(n-1))
            k = k % factorial(n-1)
            n -= 1
        n = len(ans)
        hit = [0] * n
        for i in range(n):
            count = 0
            for j in range(n):
                if not hit[j]:
                    count += 1
                if count > ans[i]:
                    ans[i] = j+1
                    hit[j] = 1
                    break
        return "".join([str(t) for t in ans])
s=Solution()
print s.getPermutation(5,96)
