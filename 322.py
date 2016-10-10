class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = 99999999
        f = [inf] * (amount+1)
        f[0] = 0
        for i in range(1, amount+1):
            f[i] = min([f[i]]+[f[i-coins[j]] + 1 for j in range(len(coins)) if i >= coins[j]])
        return f[amount]

s = Solution()
print s.coinChange([370,417,408,156,143,434,168,83,177,280,117], 9953)
