class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        add = 0
        ans = []
        for i in range(max(len(num1), len(num2))):
            a = int(num1[i]) if i < len(num1) else 0
            b = int(num2[i]) if i < len(num2) else 0
            tmp, add = (a+b+add) % 10, (a+b+add) / 10
            ans.append(str(tmp))
        if add:
            ans.append(str(add))
        return "".join(reversed(ans))

s=Solution()
print s.addStrings("11223","99999")
