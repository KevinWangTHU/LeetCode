class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchl(l, r, target):
            while l <= r:
                m = (l+r) / 2
                if numbers[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        def searchr(l, r, target):
            while l <= r:
                m = (l+r) / 2
                if numbers[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r
        l, r = 0, len(numbers)-1
        while True:
            r = min(searchr(l, r, target-numbers[l]), r)
            if numbers[l] + numbers[r] == target:
                return (l+1, r+1)
            l = searchl(l, r, target-numbers[r])
            if numbers[l] + numbers[r] == target:
                return (l+1, r+1)
s=Solution()
print s.twoSum([0,0,4], 0)
