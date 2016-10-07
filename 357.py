class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            return 0
        f = [1]
        const = [9] + range(9, 0, -1)
        for i in range(1, n):
            s = 1
            for j in range(i):
                s *= const[j]
            f.append(f[i-1] + s)
        return f[n]
