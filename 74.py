class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (matrix[0][0] <= target <= matrix[-1][-1]): return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m-1
        while l <= r:
            m = (l+r) / 2
            if matrix[m][0] <= target:
                l = m + 1
            else:
                r = m - 1

        row = matrix[r]
        l, r = 0, n-1
        while l <= r:
            m = (l+r) / 2
            if row[m] < target:
                l = m + 1
            else:
                r = m - 1
        return True if l < n and row[l] == target else False



s = Solution()
print s.searchMatrix(
    [[1],[3]],
2)
