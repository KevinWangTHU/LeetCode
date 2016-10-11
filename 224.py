class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        oplist = ["+", "-", "*", "/", "(", ")"]
        for op in oplist:
            s = s.replace(op, " " + op + " ")
        s = s.split(" ")

        stack = []
        out = []
        for c in s:
            if c == "":
                continue
            if c not in oplist:
                out.append(int(c))
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack and stack[-1] != "(":
                    out.append(stack.pop())
                stack.pop()
            elif c in ["*", "/"]:
                while stack and stack[-1] in ["*", "/"]:
                    out.append(stack.pop())
                stack.append(c)
            else:
                while stack and stack[-1] in ["+", "-", "*", "/"]:
                    out.append(stack.pop())
                stack.append(c)
        while stack:
            out.append(stack.pop())

        for c in out:
            if type(c) is str:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(a-b)
                elif c == "*":
                    stack.append(a*b)
                elif c == "/":
                    stack.append(a/b)
            else:
                stack.append(c)
        return stack[-1]
s=Solution()
print s.calculate("1+1")
