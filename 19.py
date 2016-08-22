# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd_twopass(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        h = head
        while h:
            h = h.next
            length += 1
        c = dummy
        for i in range(length - n):
            c = c.next
        c.next = c.next.next
        return dummy.next

    def removeNthFromEnd(self, head, n):
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head

        def rmv(h, n):
            if h:
                k = rmv(h.next, n)
                if k == n:
                    h.next = h.next.next
                return k+1
            else:
                return 0

        rmv(dummy, n)
        return dummy.next
