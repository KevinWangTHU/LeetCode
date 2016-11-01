class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(x, y):
            if x == y:
                return 0
            if len(x) < len(y):
                x, y = y, x
            for i in xrange(len(y)):
                if x[i] < y[i]:
                    return -1
                elif x[i] > y[i]:
                    return 1
            return compare(y, x[len(y):])
        nums = [str(num) for num in nums]
        nums.sort(reverse=True, cmp=compare)
        return "".join(nums)
s=Solution()
print s.largestNumber([3, 30, 34, 5, 9])
