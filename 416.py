class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        nums.sort(reverse=True)
        length = len(nums)
        if s % 2:
            return False
        target = s / 2
        def search(idx, cur, prevUsed):
            if cur == target:
                return True
            if idx == length:
                return False
            if cur > target:
                return False
            if not prevUsed and nums[idx] == nums[idx-1]:
                return search(idx+1, cur, False)
            else:
                return search(idx+1, cur+nums[idx], True) or search(idx+1, cur, False)
        return search(1, nums[0], True)

s=Solution()
print s.canPartition([17,58,41,75,61,70,52,7,38,11,40,58,44,45,4,81,67,54,79,80,15,3,14,16,9,66,69,41,72,37,28,3,33,90,56,12,72,49,35,22,49,27,49,82,41,77,100,82,18,95,24,51,37,2,34,82,70,53,73,32,90,98,81,22,73,76,79,40,27,62,45,96,36,15,63,28,54,88,63,37,58,9,62,98,93,72,99,53,91,29,61,31,11,42,20,35,50,68,10,86])
