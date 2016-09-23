from random import randint as randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        ret = -1
        for idx, num in enumerate(self.nums):
            if num == target:
                # this is the reservoir sampling technique
                ret = idx if randint(0, count) == 0 else ret
                count += 1
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
