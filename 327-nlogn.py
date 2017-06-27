class Solution(object):
    def s(self, i, j):
        # sum of [i, j)
        return self.sum[j] - self.sum[i]

    def getsum(self, left, right, medium):
        # include [left, right)
        leftsum = []
        rightsum = []
        for i in range(left, medium):
            leftsum.append(self.s(i, medium))
        for i in range(medium, right):
            rightsum.append(self.s(medium, i+1))
        return leftsum, rightsum


    def calc(self, left, right, upper):


    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.sum = [0]
        self.nums = nums

        for i in range(len(nums)):
            self.sum.append(self.sum[i] + nums[i])
        # s(i, j) = sum(j+1) - sum(i)

        return self.calc(0, len(nums), upper+1) - self.calc(0, len(nums), lower)
