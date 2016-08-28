class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dist = 0
        i = 0
        while i < len(nums) and i <= dist:
            if dist < i + nums[i]:
                dist = i + nums[i]
            i += 1
        if dist >= len(nums) - 1:
            return True
        else:
            return False
