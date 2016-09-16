# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tail = head
        while tail.next:
            tail = tail.next
        cur = head
        while cur is not tail:
            next = cur.next
            cur.next = tail.next
            tail.next = cur
            cur = next
        return tail
