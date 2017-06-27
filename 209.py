class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        head = tail = 0  # [head:tail]
        total, minlen = 0, 9999999
        while tail < len(nums):
            total += nums[tail]
            tail += 1
            if total >= s:
                break
        if total < s:
            return 0
        minlen = tail - head
        while True:
            while total - nums[head] >= s:
                total -= nums[head]
                head += 1
            minlen = min(tail-head, minlen)
            if tail == len(nums):
                break
            total += nums[tail]
            tail += 1
        return minlen
