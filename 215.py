# quick-select, partition
class Solution(object):
    def findKthLargest_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]

    def findKthLargest(self, nums, k):
        return self.findKthSmallest(nums, len(nums)-k+1)

    def findKthSmallest(self, nums, k):
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]

    def partition(self, nums, l, r):
        idx = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[idx] = nums[idx], nums[l]
                idx += 1
            l += 1
        nums[idx], nums[r] = nums[r], nums[idx]
        return idx

s = Solution()
s.findKthLargest([1,2,2,4,6,8,1,4,9,2,5,6], 6)
