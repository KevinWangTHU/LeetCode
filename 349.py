class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        d2 = {}
        ans = []
        for num in nums1:
            if num not in d:
                d[num] = 1
        for num in nums2:
            if num in d and num not in d2:
                ans.append(num)
                d2[num] = 1
        return ans
s = Solution()
print s.intersection([1,2,2,1], [2,2])
