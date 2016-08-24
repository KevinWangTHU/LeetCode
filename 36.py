class Solution(object):
    def isValidSudoku_straight(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def pValidator(b):
            for i in range(9):
                count = [0] * 10
                p = b[i]
                for item in p:
                    if item == 0:
                        continue
                    count[item] += 1
                    if count[item] > 1:
                        return False
            return True

        def vValidator(b):
            for i in range(9):
                count = [0] * 10
                v = [b[k][i] for k in range(9)]
                for item in v:
                    if item == 0:
                        continue
                    count[item] += 1
                    if count[item] > 1:
                        return False
            return True

        def sValidator(b):
            def valid(b, p):
                count = [0] * 10
                s = [[b[p[0]+deltax][p[1]+deltay] for deltax in range(3)] for deltay in range(3)]
                s = sum(s, [])
                for item in s:
                    if item == 0:
                        continue
                    count[item] += 1
                    if count[item] > 1:
                        return False
                return True
            points = [(x,y) for x in range(0,9,3) for y in range(0,9,3)]
            ans = True
            for p in points:
                ans = ans and valid(b, p)
            return ans

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    board[i][j] = 0
                else:
                    board[i][j] = ord(board[i][j])-48
        return pValidator(board) and vValidator(board) and sValidator(board)
