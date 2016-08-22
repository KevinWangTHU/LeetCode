class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gp(l, r):
            if l == 0:
                return [")"*r]
            if l == r:
                tmp = gp(l-1, r)
                return ["("+t for t in tmp]
            else:
                a = ["(" + t for t in gp(l-1, r)]
                b = [")" + t for t in gp(l, r-1)]
                return a+b
        # return gp(n, n)
        self.m = []
        self.gp2(n, n, "")
        return self.m
    def gp2(self, l, r, s):
        if l == 0 and r == 0:
            self.m.append(s)
        if l > 0:
            self.gp2(l-1, r, s+"(")
        if l < r:
            self.gp2(l, r-1, s+")")
