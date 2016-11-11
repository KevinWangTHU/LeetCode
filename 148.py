def printList(head):
    while head:
        print head.val
        head = head.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1 = ListNode(0)
        p2 = ListNode(0)
        cur = p1.next = head
        next = p2.next = head.next

        while next is not None:
            cur.next = next.next
            cur, next = next, cur.next
        p1.next = self.sortList(p1.next)
        p2.next = self.sortList(p2.next)

        cur1 = p1
        cur2 = p2.next
        while cur1.next and cur2:
            if cur1.next.val <= cur2.val:
                cur1 = cur1.next
            else:
                next2 = cur2.next
                cur2.next = cur1.next
                cur1.next = cur2
                cur2 = next2
        cur1.next = cur2

        return p1.next

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s=Solution()
printList(s.sortList(a))
