class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        lstack = [[-1, -9999]]
        rstack = [[-1, -9999]]
        ans = []
        for i, h in enumerate(heights):
            while lstack and lstack[-1][1] >= h:
                lstack.pop()
            ans.append(h * (i - lstack[-1][0]))
            lstack.append([i, h])
        for i, h in enumerate(reversed(heights)):
            while rstack and rstack[-1][1] >= h:
                rstack.pop()
            ans[~i] += h * (i - rstack[-1][0]) - h
            rstack.append([i, h])
        return max(ans) if ans else 0
s = Solution()
print s.largestRectangleArea([1,1])
