class Solution(object):
    def permute_heapAlgo(self, nums):
        ans = []
        def generate(n, nums):
            if n == 1:
                ans.append(nums[:])
            else:
                for i in range(n-1):
                    generate(n-1, nums)
                    if n % 2 == 0:
                        nums[i], nums[n-1] = nums[n-1], nums[i]
                    else:
                        nums[0], nums[n-1] = nums[n-1], nums[0]
                generate(n-1, nums)

        generate(len(nums), nums)
        return ans

    def permute_oneline(self, nums): # Really COOL!!!
        return [[n] + p for i, n in enumerate(nums)
                 for p in self.permute_oneline(nums[:i]+nums[i+1:])] or [[]]
