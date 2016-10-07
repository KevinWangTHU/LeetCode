from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = [(matrix[0][0], 0, 0)]
        ifIn = [[False] * len(matrix) for _ in range(len(matrix))]
        while k > 0:
            k -= 1
            item, x, y = heappop(q)

            ret = item
            if x < len(matrix) - 1 and not ifIn[x+1][y]:
                heappush(q, (matrix[x+1][y], x+1, y))
                ifIn[x+1][y] = True
            if y < len(matrix) - 1 and not ifIn[x][y+1]:
                heappush(q, (matrix[x][y+1], x, y+1))
                ifIn[x][y+1] = True
        return ret
s=Solution()
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 4)
