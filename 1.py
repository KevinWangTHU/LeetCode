from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hashtable:
                return [i, hashtable[a]]
            hashtable[nums[i]] = i
        return [-1, -1]
