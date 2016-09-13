class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        for num in nums1:
            if num not in d1:
                d1[num] = 1
            else:
                d1[num] += 1
        d2 = {}
        ans = []
        for num in nums2:
            if num in d1:
                if num not in d2:
                    d2[num] = 1
                    ans.append(num)
                elif d2[num] < d1[num]:
                    d2[num] += 1
                    ans.append(num)
        return ans
s=Solution()
print s.intersect([1,2,2,1,2,2,1], [1,2,2,2,2])
