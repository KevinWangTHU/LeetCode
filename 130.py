class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])

        for i in range(m):
            board[i] = [board[i][j] for j in range(n)]

        s = []
        for i in range(m):
            s += (i, 0), (i, n-1)
        for j in range(n):
            s += (0, j), (m-1, j)
        while s:  # beautiful part
            i, j = s.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "G"
                s += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        board[:] = [["O" if board[i][j] == "G" else "X" for j in range(n)] for i in range(m)]


s=Solution()
s.solve(["XOXOOOO",
         "XOOOOOO",
         "XOOOOXO",
         "OOOOXOX",
         "OXOOOOO",
         "OOOOOOO",
         "OXOOOOO"])
