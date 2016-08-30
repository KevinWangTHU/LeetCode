class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        nums.sort()
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            d[nums[i]] -= 1
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                d[nums[j]] -= 1
                for k in range(j+1, len(nums)-1):
                    if k != j+1 and nums[k] == nums[k-1]:
                        continue
                    f = target-nums[i]-nums[j]-nums[k]
                    if f < nums[k]:
                        break
                    d[nums[k]] -= 1
                    if f in d and d[f]:
                        ans.append([nums[i], nums[j], nums[k], f])
                    d[nums[k]] += 1
                d[nums[j]] += 1
            d[nums[i]] += 1

        return ans

s = Solution()
print s.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
