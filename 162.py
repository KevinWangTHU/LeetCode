class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) / 2
            left = -999999999999 if m == 0 else nums[m-1]
            right = -999999999999 if m == len(nums)-1 else nums[m+1]
            if nums[m] > left and nums[m] > right:
                return m
            if nums[m] < left:
                r = m - 1
            else:
                l = m + 1
        return l
s=Solution()
print s.findPeakElement([1,2,3,1])
