class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0]*n for _ in range(n)]
        count = 1
        i, j = 0, 0
        while count <= n**2:
            while j < n and mat[i][j] == 0:
                mat[i][j] = count
                count += 1
                j += 1
            i += 1
            j -= 1
            while i < n and mat[i][j] == 0:
                mat[i][j] = count
                count += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and mat[i][j] == 0:
                mat[i][j] = count
                count += 1
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and mat[i][j] == 0:
                mat[i][j] = count
                count += 1
                i -= 1
            i += 1
            j += 1
        return mat
s=Solution()
print s.generateMatrix(4)
