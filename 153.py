class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        pivot = nums[l]
        while l <= r:
            m = (l+r) / 2
            if nums[m] >= pivot:
                l = m + 1
            else:
                r = m - 1
        return pivot if l == len(nums) else nums[l]
s = Solution()
print s.findMin([4,5,5,1,1,2,3,3])
