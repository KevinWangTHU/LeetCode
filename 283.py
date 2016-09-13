class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroIdx = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0: continue
            flag = False
            for idx in range(max(i+1, idx), len(nums)):
                if nums[idx] != 0:
                    flag = True
                    break
            if flag:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
            else:
                break
        print nums
s=Solution()
s.moveZeroes([0,2,0,3,0,5,0])
