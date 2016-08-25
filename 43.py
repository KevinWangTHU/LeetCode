class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def strNum(s, num):
            # return List[int]
            c = []
            add = 0
            for i in range(len(s)):
                c.append((ord(s[i]) - 48) * num + add)
                add = c[i] / 10
                c[i] %= 10
                c[i] = c[i]
            if add > 0:
                c.append(add)
            return c
        def numNum(s1, s2):
            if len(s1) > len(s2):
                l, s = s1, s2
            else:
                l, s = s2, s1
            c = []
            add = 0
            for i in range(len(l)):
                c.append(l[i] + s[i] + add if i < len(s) else l[i] + add)
                add = c[i] / 10
                c[i] %= 10
                c[i] = c[i]
            if add > 0:
                c.append(add)
            return c

        num1, num2 = num1[::-1], num2[::-1]
        prev = []
        for i in range(len(num2)):
            digit = ord(num2[i]) - 48
            cur = [0]*i + strNum(num1, digit)
            prev = numNum(cur, prev)
        ans = ""
        for item in reversed(prev):
            ans += str(item)
        return ans

s=Solution()
print s.multiply("123456789","987654321")
