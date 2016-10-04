class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        xor -= xor & (xor-1)
        group1 = group2 = 0
        for num in nums:
            if num & xor:
                group1 ^= num
            else:
                group2 ^= num
        return [group1, group2]
