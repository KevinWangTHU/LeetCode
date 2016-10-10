import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        oplist = ["+", "-", "*", "/"]
        s = s.replace(" ", "")
        for op in oplist:
            s = s.replace(op, " " + op + " ")
        s = s.split()
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i] not in oplist:
                nums.append(int(s[i]))
            else:
                if s[i] == "*" or s[i] == "/":
                    a = nums.pop()
                    b = int(s[i+1])
                    nums.append(a*b if s[i] == "*" else a/b)
                    i += 1
                else:
                    ops.append(s[i])
            i += 1
        nums = list(reversed(nums))
        ops = list(reversed(ops))
        while ops:
            a = nums.pop()
            b = nums.pop()
            o = ops.pop()
            nums.append(a+b if o == "+" else a-b)
        return nums[0]
s=Solution()
print s.calculate("1+2*3/4-6*5/3+15")
