class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        l = len(nums)
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            if counter[num] > l//2:
                return num
        return -1

    def better_solution(self, nums):  # really smart!
        major = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                cnt = 1
                major = nums[i]
            if nums[i] == major:
                cnt += 1
            else:
                cnt -= 1
        return major
