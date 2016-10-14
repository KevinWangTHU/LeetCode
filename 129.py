# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = []
        self.ans = 0

        def search(root):
            cur.append(str(root.val))
            if not root.left and not root.right:
                self.ans += int("".join(cur))
            if root.left:
                search(root.left)
            if root.right:
                search(root.right)
            cur.pop()
        if root:
            search(root)
        return self.ans
