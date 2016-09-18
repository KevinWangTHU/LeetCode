class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix == []:
            self.s = None
            return
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.s = [[0] * (self.n+1)] + [[0] for _ in range(self.m)]
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                self.s[i].append(matrix[i-1][j-1] + self.s[i][j-1])


        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                self.s[i][j] += self.s[i-1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.s[row2+1][col2+1] + self.s[row1][col1] - self.s[row1][col2+1] \
            - self.s[row2+1][col1] if self.s else 0

s=NumMatrix([])
print s.sumRegion(1,2,2,4)
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
