# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs_bad(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head.next
        a, b = head, head.next
        while a and b:
            a.next = b.next
            b.next = a
            if a.next:
                c = a.next
                b = c.next
                if b:
                    a.next = b
                a = c
            else:
                break
        return dummy.next
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next

            a.next = b.next
            b.next = a

            cur.next = b

            cur = cur.next.next
        return dummy.next
