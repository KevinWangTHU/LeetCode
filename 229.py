class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        m1 = nums[0]
        cnt1 = 1
        m2 = 99999
        cnt2 = 1
        for cnt1 in range(1, len(nums)):
            if nums[cnt1] != m1:
                m2 = nums[cnt1]
                break

        for i in range(cnt1+cnt2, len(nums)):
            if nums[i] == m1:
                cnt1 += 1
            elif nums[i] == m2:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    m1 = nums[i]
                    cnt1 = 1
                elif cnt2 == 0:
                    m2 = nums[i]
                    cnt2 = 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == m1:
                cnt1 += 1
            elif num == m2:
                cnt2 += 1
        ans = []
        if cnt1 > len(nums)/3:
            ans.append(m1)
        if cnt2 > len(nums)/3:
            ans.append(m2)
        return ans

s= Solution()
print s.majorityElement([2,2,2,2,1,3,4,5,6,7,8,9,10])
