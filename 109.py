# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST_nlogn(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        cur = head
        count = 0
        while count < length/2 - 1:
            cur = cur.next
            count += 1
        mid = cur.next
        cur.next = None
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
    def sortedListToBST(self, head):
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        def buildTree(n):
            if n < 0:
                return None
            if n == 0:
                return TreeNode(0)
            left = n/2
            right = n - 1 - n/2
            node = TreeNode(0)
            node.left = buildTree(left)
            node.right = buildTree(right)
        root = buildTree(length)
        self.head = head
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            root.val = self.head.val
            self.head = self.head.next
            inorder(root.right)
        return root
