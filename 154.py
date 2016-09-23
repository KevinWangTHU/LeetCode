class Solution(object):
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
                return pivotL
            else:
                if ans[1] > 0:
                    l = ans[0]
                else:
                    r = ans[0]
        print l, r
        pivot = nums[r]
        rMax = r
        while l <= r:
            m = (l+r) / 2
            if nums[m] > pivot:
                l = m + 1
            else:
                r = m - 1
        return pivot if l == rMax else nums[l]
s=Solution()
print s.findMin([3,4,5,2,3,3,3,3])
