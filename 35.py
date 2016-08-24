# Actually this is lower bound binary search.
# The desired output is in [l, r+1]
#

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums-1)
        while(l <= r):
            m = (l+r) // 2  # may overflow, but this is neater
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
