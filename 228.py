class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        out = []
        if not nums:
            return out
        nums.append(-9999999999)
        cur = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == cur[1] + 1:
                cur[1] = nums[i]
            else:
                out.append(str(cur[0]) if cur[0] == cur[1] else str(cur[0])+"->"+str(cur[1]))
                cur = [nums[i], nums[i]]
        return out
s=Solution()
print s.summaryRanges([0,1,2,4,5,7])
