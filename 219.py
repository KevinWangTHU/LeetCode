class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(min(k, len(nums))):
            if nums[i] in d:
                return True
            d[nums[i]] = 1
        for i in range(k, len(nums)):
            d[nums[i-k]] -= 1
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                if d[nums[i]] > 0:
                    return True
                d[nums[i]] = 1
        return False
