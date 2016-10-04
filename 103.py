# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        left = [root]
        right = []
        while left or right:
            curLevel = []
            if left:
                right = []
                for node in reversed(left):
                    curLevel.append(node.val)
                    if node.left:
                        right.append(node.left)
                    if node.right:
                        right.append(node.right)
                left = []
            else:
                left = []
                for node in reversed(right):
                    curLevel.append(node.val)
                    if node.right:
                        left.append(node.right)
                    if node.left:
                        left.append(node.left)
                right = []
            ans.append(curLevel)
        return ans
