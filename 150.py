class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(a-b)
                elif c == "*":
                    stack.append(a*b)
                elif c == "/":
                    stack.append(int(float(a)/b))  # stupid python
            else:
                stack.append(int(c))
        return stack[-1]
s=Solution()
print s.evalRPN(["1", "-11", "/"])
