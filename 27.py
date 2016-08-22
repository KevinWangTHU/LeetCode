class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sc_idx = 0
        rp_idx = 0

        while sc_idx < len(nums):
            if nums[sc_idx] != val:
                nums[rp_idx] = nums[sc_idx]
                rp_idx += 1
            sc_idx += 1
        return rp_idx
