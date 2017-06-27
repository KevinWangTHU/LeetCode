class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: list[list[int]]
        """
        ans = []
        def dfs(k, cur):
            if k == 0:
                ans.append(cur[:])
                return
            for i in range(cur[-1] if cur else 0, n):
                cur.append(i+1)
                dfs(k-1, cur)
                cur.pop()
            return
        if k > n/2:
            dfs(n-k, [])
            newans = []
            for l in ans:
                newl = []
                idx = 0
                for num in range(1, n+1):
                    if idx >= len(l) or l[idx] != num:
                        newl.append(num)
                    else:
                        idx += 1
                newans.append(newl[:])
            return newans
        else:
            dfs(k, [])
            return ans

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def search(cur, remain):
            if remain == 0:
                return [[]]
            return [[c] + next
                    for c in range(cur, n+2-remain)
                    for next in search(c+1, remain-1)]
        return search(1, k)

s=Solution()
print s.combine2(4,2)
