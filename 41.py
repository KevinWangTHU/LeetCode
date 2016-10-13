class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > n:
                continue
            nexti = nums[i] - 1
            while 0 <= nexti < n and nums[nexti] != nexti + 1:
                temp = nums[nexti]
                nums[nexti] = nexti + 1
                nexti = temp - 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


s= Solution()
print s.firstMissingPositive([])
