# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def _flat(root):
            if not root.left and not root.right:
                return root, root
            if root.left and root.right:
                rootL, tailL = _flat(root.left)
                rootR, tailR = _flat(root.right)
                root.left = None
                root.right = rootL
                tailL.right = rootR
                return root, tailR
            if root.left:
                rootL, tailL = _flat(root.left)
                root.left = None
                root.right = rootL
                return root, tailL
            if root.right:
                _, tailR = _flat(root.right)
                return root, tailR
        if root:
            _flat(root)[0]
