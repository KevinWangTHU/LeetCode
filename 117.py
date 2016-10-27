# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level_start = root
        while level_start:
            cur = level_start
            tmp = None
            while cur:
                if cur.left and cur.right:
                    cur.left.next = cur.right
                cur_next = cur.next
                if cur.left or cur.right:
                    cur_dec = cur.right or cur.left
                    while cur_next and cur_next.left is None and cur_next.right is None:
                        cur_next = cur_next.next
                    cur_dec.next = cur_next.left or cur_next.right if cur_next else None
                    tmp = tmp or cur.left or cur.right
                cur = cur_next
            level_start = tmp

s = Solution()
a=TreeLinkNode(1)
b=TreeLinkNode(2)
c=TreeLinkNode(3)
d=TreeLinkNode(4)
e=TreeLinkNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
s.connect(a)
print d.next.val
