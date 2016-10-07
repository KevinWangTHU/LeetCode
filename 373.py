from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(nums1), len(nums2)
        if not m or not n:
            return []
        q = [(nums1[0]+nums2[0], 0, 0)]
        ifIn = [[False] * n for _ in range(m)]
        ans = []
        while k > 0 and q:
            k -= 1
            value, i, j = heappop(q)
            ans.append([nums1[i], nums2[j]])
            if i < m-1 and not ifIn[i+1][j]:
                heappush(q, (nums1[i+1]+nums2[j], i+1, j))
                ifIn[i+1][j] = True
            if j < n-1 and not ifIn[i][j+1]:
                heappush(q, (nums1[i]+nums2[j+1], i, j+1))
                ifIn[i][j+1] = True
        return ans
