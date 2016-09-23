# monotonic queue
from collections import deque as deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        ans = []
        dq = deque()
        for i in range(len(nums)):
            while len(dq) and dq[0] <= i - k:
                dq.popleft()
            while len(dq) and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i-k+1 >= 0:
                ans.append(nums[dq[0]])
        return ans

s=Solution()
print s.maxSlidingWindow([1,3,1,2,0,5],3)
