class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        global ans
        board = [["."]*n for _ in range(n)]
        ans = 0

        ifCol = [1] * n
        ifDiag = [1] * (2*n-1)  # i+j
        ifAnti = [1] * (2*n-1)  # i-j+N-1

        def dfs(i):
            global ans
            if i == n:
                ans += 1
                return
            for j in range(n):
                if ifCol[j] and ifDiag[i+j] and ifAnti[i-j+n-1]:
                    ifCol[j] = 0
                    ifDiag[i+j] = 0
                    ifAnti[i-j+n-1] = 0
                    dfs(i+1)
                    ifCol[j] = ifDiag[i+j] = ifAnti[i-j+n-1] = 1

        dfs(0)
        return ans
s = Solution()
print s.totalNQueens(4)
