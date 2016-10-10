class Solution(object):
    def maximalSquare_first(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        up, left = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(1, m):
                if matrix[i-1][j]:
                    up[i][j] = up[i-1][j] + 1
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j-1]:
                    left[i][j] = left[i][j-1] + 1
        ans = [[0] * n for _ in range(m)]
        ans[0] = matrix[0][:]
        MAX = 1 if sum(ans[0]) else 0
        for i in range(1, m):
            ans[i][0] = matrix[i][0]
            if matrix[i][0]:
                MAX = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                ans[i][j] = min(up[i][j], left[i][j], ans[i-1][j-1]) + 1
                if ans[i][j] > MAX:
                    MAX = ans[i][j]
        return MAX**2

    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        ans = [[0] * n for _ in range(m)]
        ans = [[0] * n for _ in range(m)]
        ans[0] = matrix[0][:]
        MAX = 1 if sum(ans[0]) else 0
        for i in range(1, m):
            ans[i][0] = matrix[i][0]
            if matrix[i][0]:
                MAX = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                ans[i][j] = min(ans[i-1][j], ans[i][j-1], ans[i-1][j-1]) + 1
                if ans[i][j] > MAX:
                    MAX = ans[i][j]
        return MAX**2
