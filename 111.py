# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # if there is no [] case then it can be much more elegant
    def minDepth(self, root):  # leaf node
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        if root.left or root.right:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            return 1 + l if r == 0 else 1 + r
        return 1
