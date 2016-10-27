# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        def traversal(root, depth):
            if depth == len(self.ans):
                self.ans.append(root.val)
            if root.right:
                traversal(root.right, depth+1)
            if root.left:
                traversal(root.left, depth+1)
        if root:
            traversal(root, 0)
        return self.ans
