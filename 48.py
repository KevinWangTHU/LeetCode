class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range((N+1)//2):
            for j in range(N/2):
                matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] \
                    = matrix[N-j-1][i], matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]
