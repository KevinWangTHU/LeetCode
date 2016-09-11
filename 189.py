from fractions import gcd as gcd
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        group = gcd(len(nums), k)
        for i in range(group):
            prevIdx = i
            prevNum = nums[prevIdx]
            for cnt in range(len(nums)/group):
                curIdx = (prevIdx + k) % len(nums)
                nums[curIdx], prevNum = prevNum, nums[curIdx]
                prevIdx = curIdx
