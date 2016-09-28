# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        vis = {}
        s = [root]
        ans = []
        while s:
            cur = s.pop()
            if cur in vis:
                ans.append(cur.val)
                continue
            if cur.right:
                s.append(cur.right)
            vis[cur] = True
            s.append(cur)
            if cur.left:
                s.append(cur.left)
        return ans
