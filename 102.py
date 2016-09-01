# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def search(root, depth):
            if depth < len(traversal):
                traversal[depth].append(root.val)
            else:
                traversal.append([root.val])
            if root.left:
                search(root.left, depth+1)
            if root.right:
                search(root.right, depth+1)

        traversal = []
        if root:
            search(root, 0)
            return traversal
        else:
            return []
