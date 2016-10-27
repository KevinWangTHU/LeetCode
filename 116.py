# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):  # requires O(1) space
        level_start = root
        while level_start and level_start.left:
            cur = level_start
            while cur:
                cur.left.next = cur.right
                if cur.next is not None:
                    cur.right.next = cur.next.left
                cur = cur.next
            level_start = level_start.left
        return
