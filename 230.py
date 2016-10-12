# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        global count
        count = 0
        ans = -1
        def dfs(root):
            global count
            if not root.left and not root.right:
                count += 1
                if count == k:
                    return root.val
                return None
            if root.left:
                a = dfs(root.left)
                if a is not None:
                    return a
            count += 1
            if count == k:
                return root.val
            if root.right:
                b = dfs(root.right)
                if b is not None:
                    return b
            return None
        return dfs(root)
