class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(idx, remain, cur):
            if remain == 0:
                ans.append(cur[:])
                return
            cur.append(nums[idx])
            dfs(idx+1, remain-1, cur)
            cur.pop()
            if remain < len(nums) - idx:
                dfs(idx+1, remain, cur)

        for l in range(len(nums)+1):
            dfs(0, l, [])
        return ans
s=Solution()
s.subsets([1,2,3])
