class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            l, s = a, b
        else:
            l, s = b, a

        l, s = list(reversed(l)), list(reversed(s))
        ret = []
        d3 = 0
        for i in range(len(l)):
            d1 = ord(l[i]) - 48
            d2 = ord(s[i]) - 48 if i < len(s) else 0
            d1, d3 = d1 ^ d2 ^ d3, (d1 & d2) | (d3 & (d1 ^ d2))
            ret.append(str(d1))
        if d3:
            ret.append(str(d3))
        return "".join(list(reversed(ret)))
