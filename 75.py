class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for p0 in range(len(nums)):
            if nums[p0] != 0:
                break
        for p2 in range(len(nums)-1, -1, -1):
            if nums[p2] != 2:
                break
        i = p0
        print p0, p2
        while i <= p2:
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                while p2 >= 0 and nums[p2] == 2:
                    p2 -= 1
        print nums
s=Solution()
s.sortColors([2,2,2])
