import math, random
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        self.n = len(nums)
        self.sortedNums = sorted(self.nums)
        self.used = [False] * self.n

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.used = [False] * self.n



    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = []
        nFac = math.factorial(self.n)
        shuffleNum = random.randint(0, nFac-1)
        print shuffleNum
        for i in range(self.n):
            nFac /= (self.n-i)
            nIdx = shuffleNum / nFac
            shuffleNum = shuffleNum % nFac
            count = 0
            for j in range(self.n):
                if count == nIdx and not self.used[j]:
                    self.used[j] = True
                    break
                if not self.used[j]:
                    count += 1
            ans.append(self.sortedNums[j])
        return ans

s = Solution([1,2,3,4,5])
print s.shuffle()
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
