# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = [root] if root else []
        while s:
            cur = s.pop()
            ans.append(cur.val)
            if cur.right:
                s.append(cur.right)
            if cur.left:
                s.append(cur.left)
        return ans
