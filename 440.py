from math import log, ceil
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(prefix):
            digit = int(log(n, 10)+0.0001) - int(log(prefix, 10) + 0.0001)
            if not digit:
                return 1
            ret = int("1" * digit) + (10**digit if n > (prefix+1)*10**digit else n-(prefix*10**digit)+1 if n >= prefix*10**digit else 0)
            return ret
        ans = 1
        while k > 1:
            num = count(ans)
            if num < k:
                ans += 1
                k -= num
            else:
                ans *= 10
                k -= 1
        return ans

s=Solution()
print s.findKthNumber(1000, 123)
