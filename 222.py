# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def haveNode(num, depth, root):
    while depth > 1:
        p = 2**(depth - 1)
        if num // p == 0:
            root = root.left
        else:
            root = root.right
        num = num % p
        depth -= 1
    if num == 0:
        return root.left is not None
    else:
        return root.right is not None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 0
        head = root
        while head.left is not None:
            head = head.left
            depth += 1

        l = 0
        r = 2 ** depth
        while r - l > 1:
            m = (l+r) // 2
            if haveNode(m, depth, root):
                l = m
            else:
                r = m
        return 2**depth + l
