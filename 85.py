class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def process(heights):
            ls, rs = [(-1, -999)], [(-1, -999)]
            ans = []
            for i, h in enumerate(heights):
                while ls[-1][1] >= h:
                    ls.pop()
                ans.append(h * (i - ls[-1][0]))
                ls.append((i, h))
            for i, h in enumerate(reversed(heights)):
                while rs[-1][1] >= h:
                    rs.pop()
                ans[~i] += h * (i - rs[-1][0]) - h
                rs.append((i, h))
            return max(ans) if ans else 0

        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        height = matrix[0][:]
        ans = process(height)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            ans = max(ans, process(height))
        return ans

s = Solution()
print s.maximalRectangle(["10100","10111","11111","10010"])
