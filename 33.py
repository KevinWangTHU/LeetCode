class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        def find_rotate(nums):
            if nums[0] <= nums[-1]:
                return 0
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l+r) / 2
                if nums[m] < nums[0]:
                    r = m - 1
                else:
                    l = m + 1
            return l

        def bs(l, r, nums, target):
            while l <= r:
                m = (l+r) / 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            if 0 <= l < len(nums):
                if nums[l] == target:
                    return l

            return -1

        idx = find_rotate(nums)

        if target > nums[-1]:
            return bs(0, idx-1, nums, target)
        else:
            return bs(idx, len(nums)-1, nums, target)


s = Solution()
print s.search([4,5,6,7,0,1,2], 3)