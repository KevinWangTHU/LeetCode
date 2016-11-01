class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(b, i, j):
            if i == 9:
                return True
            nextj = j+1 if j < 8 else 0
            nexti = i if j < 8 else i+1

            if b[i][j] != ".":
                return dfs(b, nexti, nextj)
            for k in range(9):
                if not self.pUsed[i][k] and not self.vUsed[j][k] \
                   and not self.sUsed[i/3][j/3][k]:
                    self.pUsed[i][k] = self.vUsed[j][k] = self.sUsed[i/3][j/3][k] = True
                    b[i][j] = str(k+1)
                    if dfs(b, nexti, nextj):
                        return True
                    b[i][j] = "."
                    self.pUsed[i][k] = self.vUsed[j][k] = self.sUsed[i/3][j/3][k] = False
            return False

        self.pUsed = [[False] * 9 for i in range(9)]
        self.vUsed = [[False] * 9 for i in range(9)]
        self.sUsed = [[[False] * 9 for i in range(3)] for j in range(3)]
        # init

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    k = ord(board[i][j]) - 49
                    self.pUsed[i][k] = True
                    self.vUsed[j][k] = True
                    self.sUsed[i/3][j/3][k] = True
        dfs(board, 0, 0)
        for b in board:
            print b
s = Solution()

b=["....134..",".8...695.","65.......","96.2.1...","1...7...2","...3.4.16",".......79",".258...4.","..976...."]

b = [[b[i][j] for j in range(9)] for i in range(9)]
s.solveSudoku(b)
