# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead = ListNode(0)

        cur = head
        while cur:
            newcur = newhead
            while newcur.next and newcur.next.val < cur.val:
                newcur = newcur.next
            cur.next = newcur.next
            newcur.next = cur
            cur = cur.next
        return newhead.next
