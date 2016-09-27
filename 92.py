# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        count = 1
        cur = dummy
        while count < m:
            cur = cur.next
            count += 1
        prev = cur
        cur = cur.next
        while count < n:
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
            count += 1
