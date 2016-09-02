# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(root):
            if root is None:
                return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1  # do not forget +1

        if root is None:
            return True
        cond1 = self.isBalanced(root.left) and self.isBalanced(root.right)
        if cond1:
            return abs(getHeight(root.left) - getHeight(root.right)) < 2
        return False
