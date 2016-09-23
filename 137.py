class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums[0]
        B = 0
        C = ~nums[0]
        for i in range(1, len(nums)):
            A, B, C = A^(A&nums[i]) | C & nums[i], B^(B&nums[i]) | A & nums[i], C^(C&nums[i]) | B & nums[i]
        return A
