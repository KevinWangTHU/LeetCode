# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def dfs(root):
    if root is None:
        return (0, 0)
    left = dfs(root.left)
    right = dfs(root.right)
    ans = (root.val+left[1]+right[1], max(left[0], left[1])+max(right[0], right[1]))
    return ans


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(dfs(root))
