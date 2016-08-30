class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(node): # if there is circle beginning with node
            if dfsed[node]:
                return False
            if vis[node]:
                return True
            ans = False
            vis[node] = True
            for tail in edges[node]:
                ans |= dfs(tail)
            vis[node] = False
            dfsed[node] = True
            return ans

        vis = [False] * numCourses
        edges = [[] for i in range(numCourses)]
        dfsed = [False] * numCourses  # Use this to speed-up
        for h, t in prerequisites:
            edges[h].append(t)

        for node in range(numCourses):
            if dfs(node):
                return False

        return True
