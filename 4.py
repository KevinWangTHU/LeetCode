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
        def query(array, idx):
            if idx < 0:
                return -99999999
            if idx >= len(array):
                return 99999999
            return array[idx]
        m, n = len(nums1), len(nums2)
        k, is_odd = (m+n-1) / 2, (m+n) % 2

        if not m:
            return nums2[k] if is_odd else sum(nums2[k:k+2]) / 2.
        if not n:
            return nums1[k] if is_odd else sum(nums1[k:k+2]) / 2.

        l, r = -1, m

        while True:
            p, q = (l+r) / 2, k - (l+r)/2 - 1

            a = query(nums1, p)
            b = query(nums1, p+1)
            c = query(nums2, q)
            d = query(nums2, q+1)
            if max(a, c) <= min(b, d):
                return max(a, c) if is_odd else (max(a, c)+min(b, d)) / 2.
            if a > d:
                r = p
            elif c > b:
                l = p + 1

s = Solution()
print s.findMedianSortedArrays([2,], [1])
