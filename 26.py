class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rp_idx = 1
        sc_idx = 1
        while sc_idx < len(nums):
            if nums[sc_idx] > nums[sc_idx-1]:
                nums[rp_idx] = nums[sc_idx]
                rp_idx += 1
            sc_idx += 1
        return min(rp_idx, len(nums))
