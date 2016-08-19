class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p in ["(", "[", "{"]:
                stack.append(p)
            else:
                if stack == []:
                    return False
                if (p == ")" and stack[-1] == "(") or (p == "]" and stack[-1] == "[") or (p == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True
