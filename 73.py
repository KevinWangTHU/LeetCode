class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row = [1] * m
        col = [1] * n
        # Use -1 as marker to implement an O(1) space algo
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 0
        for i in range(len(row)):
            if not row[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(len(col)):
            if not col[j]:
                for i in range(m):
                    matrix[i][j] = 0
