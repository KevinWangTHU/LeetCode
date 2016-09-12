# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-999999)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            while cur.next and cur.next.val == val:  # Note Here!!!
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next
