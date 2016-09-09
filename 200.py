class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find(dset, p):
            if dset[p[0]][p[1]] == p:
                return p
            root = p
            while dset[root[0]][root[1]] != root:
                root = dset[root[0]][root[1]]

            cur = p
            while dset[cur[0]][cur[1]] != cur:
                parent = dset[cur[0]][cur[1]]
                dset[cur[0]][cur[1]] = root
                cur = parent
            return root

        def union(dset, p1, p2):
            root1 = find(dset, p1)
            root2 = find(dset, p2)
            dset[root2[0]][root2[1]] = root1

        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dset = [[(i, j) for j in range(n)] for i in range(m)]

        for i, line in enumerate(grid):
            for j, point in enumerate(line):
                if point == '0':
                    continue
                if i > 0 and grid[i-1][j] == '1':
                    union(dset, (i-1, j), (i, j))
                if j > 0 and grid[i][j-1] == '1':
                    union(dset, (i, j-1), (i, j))


        d = {}
        count = 0
        for i, line in enumerate(dset):
            for j, point in enumerate(line):
                if grid[i][j] == "0":
                    continue
                root = find(dset, point)
                if root in d:
                    continue
                d[root] = 1
                count += 1

        return count

s = Solution()
print s.numIslands([])
