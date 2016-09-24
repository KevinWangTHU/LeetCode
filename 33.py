class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bs(l, r):
            while l <= r:
                m = (l+r) / 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            if l < len(nums) and nums[l] == target:
                return l
            else:
                return -1
        l, r = 0, len(nums) - 1
        pivot = nums[r]
        while l <= r:
            m = (l+r) / 2
            if nums[m] <= pivot:
                r = m - 1
            else:
                l = m + 1
        if nums[l] == target:
            return l
        if l == 0:
            return bs(1, len(nums)-1)
        if l == len(nums):
            return bs(0, l-1)
        return bs(0, l-1) if target >= nums[0] else bs(l+1, len(nums)-1)
