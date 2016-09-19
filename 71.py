class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = path.split("/")
        print paths
        for folder in paths:
            if folder == "" or folder == ".":
                continue
            elif folder == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return "/"+"/".join(stack)
s=Solution()
print s.simplifyPath("/home/")
