class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0]*n for _ in range(m)]
        for j in range(n):
            if obstacleGrid[0][j]:
                break
            f[0][j] = 1
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            f[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i][j-1] + f[i-1][j]
        return f[m-1][n-1]
