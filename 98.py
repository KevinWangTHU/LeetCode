# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ifValid(root, Min, Max):
            if not root:
                return True
            if Min < root.val < Max:
                return ifValid(root.left, Min, root.val)  and ifValid(root.right, root.val, Max)
            else:
                return False
        return ifValid(root, -99999999, 99999999)
