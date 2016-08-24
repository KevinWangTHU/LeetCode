class Solution(object):
    def searchRange_lowerandupperboundbinarysearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lower
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if l == len(nums) or nums[l] != target:
            return [-1,-1]
        retl = l
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        retr = r
        return [retl, retr]

    def searchRange_myself(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs(nums, target, l, r):
            # l and r are included.
            if l <= r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    return bs(nums, target, m+1, r)
                else:
                    return bs(nums, target, l, m-1)
            else:
                return -1
        pivot = bs(nums, target, 0, len(nums)-1)
        if pivot == -1:
            return [-1, -1]
        left = right = pivot
        while bs(nums, target, 0, left-1) != -1:
            left = bs(nums, target, 0, left)
        while bs(nums, target, right+1, len(nums)-1) != -1:
            right = bs(nums, target, right+1, len(nums)-1)
        return [left, right]
