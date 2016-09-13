# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        if root.left is None:
            ret = self.binaryTreePaths(root.right)
        elif root.right is None:
            ret = self.binaryTreePaths(root.left)
        else:
            ret = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        for i in range(len(ret)):
            ret[i] = str(root.val)+"->"+ret[i]
        return ret
