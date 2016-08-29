class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def getMax(nums, k):
            stack = []
            for i, num in enumerate(nums):
                while stack and len(stack) + len(nums) - i > k \
                      and stack[-1] < num:
                    stack.pop()
                if len(stack) < k:
                    stack.append(num)
            return stack

        def merge(nums1, nums2):
            def greater(nums1, nums2, i, j):
                while i < len(nums1) and j < len(nums2) \
                      and nums1[i] == nums2[j]:
                    i += 1
                    j += 1
                return j == len(nums2) or i < len(nums1) \
                    and nums1[i] > nums2[j]
            nums = []
            i, j = 0, 0
            for r in range(len(nums1)+len(nums2)):
                if greater(nums1, nums2, i, j):
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            return nums

        ans = []
        for i in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            a, b = getMax(nums1, i), getMax(nums2, k-i)
            ans = max(merge(a, b), ans)
        return ans
