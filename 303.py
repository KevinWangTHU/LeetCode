class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sumI = [0]
        s = 0
        for num in nums:
            s += num
            self.sumI.append(s)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumI[j+1] - self.sumI[i]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
s = NumArray([-2,0,3,-5,2,-1])
print s.sumRange(0,5)
