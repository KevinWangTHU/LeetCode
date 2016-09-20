class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(i1, j1, i2, j2):
            print i1, j1, i2, j2
            if i1 > i2 or j1 > j2:
                return False
            if i1 == i2 and j1 == j2:
                return True if matrix[i1][j1] == target else False
            if i1 == i2:
                lo, hi = j1, j2
                while lo <= hi:
                    mid = (lo + hi) / 2
                    if matrix[i1][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                return False if hi > j2 or matrix[i1][hi] != target else True

            if j1 == j2:
                lo, hi = i1, i2
                while lo <= hi:
                    mid = (lo + hi) / 2
                    if matrix[mid][j1] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                return False if hi > i2 or matrix[hi][j1] != target else True
            m = (j1 + j2) / 2
            smallPivot = matrix[i1][m]
            largePivot = matrix[i2][m]
            if target < smallPivot:
                return search(i1, j1, i2, m-1)
            elif target > largePivot:
                return search(i1, m+1, i2, j2)
            else:
                lo, hi = i1, i2
                while lo <= hi:
                    mid = (lo + hi) / 2
                    if matrix[mid][m] >= target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                if matrix[lo][m] == target:
                    return True
                return search(lo, j1, i2, m-1) or search(i1, m+1, lo-1, j2)
        return search(0, 0, len(matrix)-1, len(matrix[0])-1)
s = Solution()
print s.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 15)
