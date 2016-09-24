class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def bs(l, r):
            while l <= r:
                m = (l+r) / 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            if l < len(nums) and nums[l] == target:
                return True
            else:
                return False
        minIdx = self.findMin(nums)
        if nums[minIdx] == target:
            return True
        if minIdx == 0:
            return bs(1, len(nums)-1)
        if minIdx == len(nums) - 1:
            return bs(0, minIdx-1)
        return bs(0, minIdx-1) if target >= nums[0] else bs(minIdx+1, len(nums)-1)
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        pivotL = nums[l]
        pivotR = nums[r]
        def search(l, r):
            if l > r:
                return None
            if l == r:
                return None if nums[l] == pivotL else (l, 1) if nums[l] > pivotL else (l, -1)
            m = (l + r) / 2
            if nums[m] > pivotL:
                return (m, 1)
            elif nums[m] < pivotL:
                return (m, -1)
            else:
                return search(l, m-1) or search(m+1, r)
        if pivotL == pivotR:
            ans = search(0, len(nums)-1)
            if ans is None:
                return 0
            else:
                if ans[1] > 0:
                    l = ans[0]
                else:
                    r = ans[0]
        pivot = nums[r]
        rMax = r
        while l <= r:
            m = (l+r) / 2
            if nums[m] > pivot:
                l = m + 1
            else:
                r = m - 1
        return r if l == rMax else l
s=Solution()
print s.search([1],0)
