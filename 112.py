# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False  # stupid test case
        if root.left is None and root.right is None:
            return True if root.val == sum else False
        ans = False
        if root.left:
            ans = ans or self.hasPathSum(root.left, sum-root.val)
        if root.right:
            ans = ans or self.hasPathSum(root.right, sum-root.val)
        return ans
