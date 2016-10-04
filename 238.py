class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        base = 1
        for num in nums:
            output.append(base*num)
            base *= num
        base = 1
        for i in range(len(nums)-1, 0, -1):
            output[i] = output[i-1] * base
            base *= nums[i]
        output[0] = base
        return output
