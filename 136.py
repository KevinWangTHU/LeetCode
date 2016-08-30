class Solution(object):
    def singleNumber_hash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for item in nums:
            if item in d:
                d[item] = 0
            else:
                d[item] = 1
        for item in d.keys():
            if d[item] == 1:
                return item

    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans
