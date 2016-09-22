class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative = False
        if numerator*denominator < 0:
            negative = True
            numerator = abs(numerator)
            denominator = abs(denominator)
        recur = False
        d = {}
        right = []
        left = numerator / denominator
        num = numerator % denominator * 10
        de = denominator
        i = 0
        while num != 0:
            if num in d:
                recur = True
                startPoint = d[num]
                break
            d[num] = i
            right.append(str(num/de))
            num = num % de
            i += 1
            num *= 10
        left = "-"+str(left) if negative else str(left)
        return left+"."+"".join(right[:startPoint])+"("+"".join(right[startPoint:])+")" if recur else left+"."+"".join(right) if right else left

s=Solution()
print s.fractionToDecimal(1,-8)
