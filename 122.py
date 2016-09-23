class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]])

s=Solution()
print s.maxProfit([3,5,6,7,2,5])
