# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        d = {}
    def cloneGraph(self, node):
        d = {}
        def dfs(node):
            root = UndirectedGraphNode(node.label)
            d[root.label] = root
            for des in node.neighbors:
                if des.label not in d:
                    d[des.label] = dfs(des)
                root.neighbors.append(d[des.label])
            return root
        return dfs(node) if node else None

g = UndirectedGraphNode(-1)
h = UndirectedGraphNode(1)
g.neighbors = [h]
s = Solution()
a = s.cloneGraph(g)
print a.label
