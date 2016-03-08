# Checked Discuss #
# Binary Search - need more practice
# Not that hard actually!!

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        inf = 99999999
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        k = (m+n) // 2

        nums1.append(inf)
        nums2.append(inf)
        nums1.insert(0, -inf)
        nums2.insert(0, -inf)

        j = n
        i = k - n
        l, r = 0, n+1

        # print nums1, nums2
        while not (min(nums1[i+1], nums2[j+1]) >= max(nums1[i], nums2[j])):
            # print j
            if (max(nums1[i], nums2[j]) == nums2[j]):
                r = j
                j = l + (j - l) // 2
                i = k - j
            else:
                l = j
                j = j + (r - j) // 2
                i = k - j

        if (m+n) % 2 == 0:
            return (max(nums1[i], nums2[j])+min(nums1[i+1], nums2[j+1]))/2.0
        return min(nums1[i+1], nums2[j+1])

s = Solution()
print s.findMedianSortedArrays([1,4,5],[2,3,6])
