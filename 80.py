class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        c = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[p-1]:
                nums[p] = nums[i]
                c = 1
                p += 1
                length += 1
            else:
                if c < 2:
                    nums[p] = nums[i]
                    p += 1
                    c += 1
                    length += 1
        return min(length, len(nums))

s=Solution()
print s.removeDuplicates([1,1,1,2,2,3])
