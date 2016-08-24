# There are four steps in this algorithm:
# 1. find the largest k such that a[k]<a[k+1]
# 2. find the largest i such that a[k]<a[i]
# 3. swap(a[k],a[i])
# 4. reverse(a,k+1,n-1)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(lst):
            for i in range(len(lst)//2):
                lst[i], lst[-i-1] = lst[-i-1], lst[i]


        idx = len(nums)-1
        while idx > 0 and nums[idx-1] >= nums[idx]:
            idx -= 1
        if idx == 0:
            reverse(nums)
        else:
            pivot = idx-1
            idx = len(nums) - 1
            while idx > 0 and nums[idx] <= nums[pivot]:
                idx -= 1
            nums[idx], nums[pivot] = nums[pivot], nums[idx]
            for i in range((len(nums)-pivot-1)//2):
                nums[i+pivot+1], nums[-i-1] = nums[-i-1], nums[i+pivot+1]
