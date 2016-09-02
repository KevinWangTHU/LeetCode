class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minNum = 9999999
        profit = 0
        for num in prices:
            if num - minNum > profit:
                profit = num - minNum
            if num < minNum:
                minNum = num

        return profit
