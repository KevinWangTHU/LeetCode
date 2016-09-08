class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l2, h2 = [2], 0
        l3, h3 = [3], 0
        l5, h5 = [5], 0
        ans = 1
        while n > 0:
            n -= 1
            if l2[h2] < l3[h3] and l2[h2] < l5[h5]:
                ans = l2[h2]
                h2 += 1
            elif l3[h3] < l2[h2] and l3[h3] < l5[h5]:
                ans = l3[h3]
                h3 += 1
            else:
                ans = l5[h5]
                h5 += 1
            l2.append(2*ans)
            l3.append(3*ans)
            l5.append(5*ans)
        return ans
