class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [nums[0]]
        g = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                f.append(0)
                g.append(0)
            elif nums[i] > 0:
                if f[i-1] > 1:
                    f.append(f[i-1]*nums[i])
                else:
                    f.append(nums[i])
                if g[i-1] < 0:
                    g.append(g[i-1]*nums[i])
                else:
                    g.append(nums[i])
            else:
                if f[i-1] > 1:
                    g.append(f[i-1]*nums[i])
                else:
                    g.append(nums[i])
                if g[i-1] < 0:
                    f.append(g[i-1]*nums[i])
                else:
                    f.append(nums[i])
        return max(f)
    def maxProduct_clean(self, nums):
        r = nums[0]
        Max = Min = r
        for i in range(1, len(nums)):
            if nums[i] < 0:
                Max, Min = Min, Max
            Max = max(Max*nums[i], nums[i])
            Min = min(Min*nums[i], nums[i])
            r = max(Max, r)
        return r

s = Solution()
print s.maxProduct_clean([-3,0,3,2,-3])
