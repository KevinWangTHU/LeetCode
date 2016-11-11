# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum_MLE(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        f = {}

        def search(root, k):
            if root is None:
                return 0
            if (root, k) not in f:
                f[(root, k)] = (1 if root.val == k else 0) + search(root.left, k-root.val) + search(root.right, k-root.val)
            return f[(root, k)]
        def out(root):
            if root is None:
                return 0
            return search(root, sum) + out(root.left) + out(root.right)
        return out(root)

    def pathSum(self, root, sum):
        f = {0: 1}
        count = [0]
        def search(root, pathsum, target):
            if not root:
                return
            pathsum += root.val
            if pathsum - target in f:
                count[0] += f[pathsum-target]
            if pathsum in f:
                f[pathsum] += 1
            else:
                f[pathsum] = 1
            search(root.left, pathsum, target)
            search(root.right, pathsum, target)
            f[pathsum] -= 1
        search(root, 0, sum)
        return count[0]
