# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = ListNode(0)
        second.next = slow.next
        slow.next = None
        cur = second.next
        while cur.next:
            tmp = cur.next.next
            cur.next.next, second.next = second.next, cur.next
            cur.next = tmp
        cur1, cur2 = head, second.next
        while cur2:
            tmp = cur2.next
            cur1.next, cur2.next = cur2, cur1.next
            cur1 = cur2.next
            cur2 = tmp
