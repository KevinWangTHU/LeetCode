class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(n):
            for item in reversed(ans):
                ans.append(item+2**i)
        return ans
s=Solution()
print s.grayCode(1)
