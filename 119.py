class Solution(object):
    triangle = [[1]]
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows < len(Solution.triangle):
            return Solution.triangle[:numRows]
        for i in range(len(Solution.triangle), numRows):
            cur = Solution.triangle[i-1]
            next = [1] + [cur[j] + cur[j+1] for j in range(len(cur)-1)] + [1]
            Solution.triangle.append(next)
        return Solution.triangle
    def getRow(self, rowIndex):
        self.generate(rowIndex+1)
        return Solution.triangle[rowIndex]
