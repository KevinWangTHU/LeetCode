# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def traversal(root, k):
    total_num = 0
    if root.left is not None:
        total_num, target = traversal(root.left, k)
        if target is not None:
            return -1, target
    if total_num == k-1:
        return -1, root.val
    total_num += 1
    if root.right is not None:
        right_num, target = traversal(root.right, k-total_num)
        total_num += right_num
        if target is not None:
            return -1, target
    return total_num, None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return traversal(root, k)[1]

    def kthSmallest_2(self, root, k):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while k > 0:
            item = stack.pop()
            succ = item.right
            while succ:
                stack.append(succ)
                succ = succ.left
            k -= 1
        return item.val


