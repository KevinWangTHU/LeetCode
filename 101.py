# Non-iterative is using stack: every time push a [left, right] pair
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ifSym_recur(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val == b.val:
                return ifSym_recur(a.left, b.right) \
                    and ifSym_recur(a.right, b.left)
            return False

        return True if not root else ifSym_recur(root.left, root.right)
