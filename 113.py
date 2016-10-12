# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        def search(root, cur, s):
            if s == sum and not root.left and not root.right:
                ans.append(cur[:])
            if root.left:
                cur.append(root.left.val)
                search(root.left, cur, s+root.left.val)
                cur.pop()
            if root.right:
                cur.append(root.right.val)
                search(root.right, cur, s+root.right.val)
                cur.pop()
        search(root, [root.val], root.val)
        return ans
