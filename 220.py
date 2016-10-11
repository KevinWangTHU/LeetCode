class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = {}
        w = t + 1
        keep = []
        head = 0
        for i in range(len(nums)):
            pos = nums[i] / w
            if pos in d:
                return True
            if pos + 1 in d and d[pos+1] - nums[i] <= t:
                return True
            if pos - 1 in d and nums[i] - d[pos-1] <= t:
                return True
            d[pos] = nums[i]
            keep.append(pos)
            if len(keep) - head > k:
                del d[keep[head]]
                head += 1
        return False

s=Solution()
print s.containsNearbyAlmostDuplicate([3,6,9,2,8], 2, 1)
