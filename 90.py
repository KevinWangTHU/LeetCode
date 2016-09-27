class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        keys = sorted(d.keys())
        ans = []
        def search(idx, remain, cur):
            if remain == 0:
                ans.append(cur)
                return
            if idx == len(keys):
                return
            for i in range(min(remain, d[keys[idx]])+1):
                search(idx+1, remain-i, cur+[keys[idx]] * i)
        for i in range(len(nums)+1):
            search(0, i, [])
        return ans
s=Solution()
print s.subsetsWithDup([1,2,2])
