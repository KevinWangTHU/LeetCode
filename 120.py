class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ans = triangle[0]
        for i in range(1, len(triangle)):
            cur = [triangle[i][0]+ans[0]]
            for j in range(1, len(triangle[i])-1):
                cur.append(min(ans[j-1], ans[j]) + triangle[i][j])
            cur.append(ans[i-1] + triangle[i][i])
            ans = cur
        return min(ans)
s=Solution()
print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
