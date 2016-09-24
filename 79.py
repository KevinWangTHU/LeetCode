class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        vis = [[False]*n for _ in range(m)]
        def search(i, j, idx):
            ret = False
            if board[i][j] == word[idx]:
                if idx == len(word) - 1:
                    return True
                vis[i][j] = True
                if i > 0 and not vis[i-1][j]:
                    ret = ret or search(i-1, j, idx+1)
                if j > 0 and not vis[i][j-1]:
                    ret = ret or search(i, j-1, idx+1)
                if i < m - 1 and not vis[i+1][j]:
                    ret = ret or search(i+1, j, idx+1)
                if j < n - 1 and not vis[i][j+1]:
                    ret = ret or search(i, j+1, idx+1)
                vis[i][j] = False
            return ret
        ans = False
        for i in range(m):
            for j in range(n):
                ans = ans or search(i, j, 0)
                if ans:
                    return ans
        return ans
s = Solution()
print s.exist(["ABCE","SFCS","ADEE"],
"ABCCED")
