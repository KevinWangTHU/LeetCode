class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s, n = sum(A), len(A)
        initial = sum([i*A[i] for i in range(len(A))])
        MAX = initial
        replace = n-1
        while replace > 0:
            initial = initial - n * A[replace] + s
            if initial > MAX:
                MAX = initial
            replace -= 1
        return MAX
s = Solution()
print s.maxRotateFunction([4,3,2])
