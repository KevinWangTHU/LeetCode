class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["."]*n for _ in range(n)]
        ans = []

        ifCol = [1] * n
        ifDiag = [1] * (2*n-1)  # i+j
        ifAnti = [1] * (2*n-1)  # i-j+N-1

        def dfs(i):
            if i == n:
                b = [r[:] for r in board]
                ans.append(b)
                return
            for j in range(n):
                if ifCol[j] and ifDiag[i+j] and ifAnti[i-j+n-1]:
                    ifCol[j] = 0
                    ifDiag[i+j] = 0
                    ifAnti[i-j+n-1] = 0
                    board[i][j] = "Q"
                    dfs(i+1)
                    ifCol[j] = ifDiag[i+j] = ifAnti[i-j+n-1] = 1
                    board[i][j] = "."

        dfs(0)
        ans = [["".join(r) for r in sol] for sol in ans]
        return ans
s = Solution()
print s.solveNQueens(8)
