class Solution(object):
    def permuteUnique_old(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [nums]
        while self.nextPermutation(nums) != ans[0]:
            nums = self.nextPermutation(nums)
            ans.append(nums)
        return ans


    def nextPermutation(self, nums):
        idx = len(nums)-1
        while idx > 0 and nums[idx-1] >= nums[idx]:
            idx -= 1
        if idx == 0:
            return nums[::-1]
        else:
            pivot = idx-1
            idx = len(nums) - 1
            while idx > 0 and nums[idx] <= nums[pivot]:
                idx -= 1

            ans = nums[:]
            ans[idx], ans[pivot] = ans[pivot], ans[idx]
            ans = ans[:pivot+1] + ans[:pivot:-1]
            return ans

    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication
                ans = new_ans
        return ans

s=Solution()
print s.permuteUnique([1,1,2,2])
