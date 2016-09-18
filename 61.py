# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        k = k % length
        k = (length - k) % length
        if not k: return head
        count = 0
        newhead = head
        while count < k:
            count += 1
            prev = newhead
            newhead = newhead.next
        prev.next = None
        cur = newhead
        while cur.next:
            cur = cur.next
        cur.next = head
        return newhead
