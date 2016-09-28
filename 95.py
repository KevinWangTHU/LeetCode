# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(p, q):
            if p > q:
                return [None]
            if p == q:
                return [TreeNode(p)]
            else:
                ans = []
                for pivot in range(p, q+1):
                    left = generate(p, pivot - 1)  # list
                    right = generate(pivot + 1, q)  # list
                    for l in left:
                        for r in right:
                            cur = TreeNode(pivot)
                            cur.left = l
                            cur.right = r
                            ans.append(cur)
        return generate(1,n)
