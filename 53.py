class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [0]
        MAX = -999999
        MIN = 0
        for num in nums:
            cur = s[-1] + num
            s.append(cur)
            if cur - MIN > MAX:
                MAX = cur - MIN
            if cur < MIN:
                MIN = cur
        return MAX

s = Solution()
print s.maxSubArray([1,2,4,-1,-5,2,-8,5,-3,6])
