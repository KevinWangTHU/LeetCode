# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            next = cur.next
            ifDup = False
            while next.next and next.val == next.next.val:
                next = next.next
                ifDup = True
            next = next.next
            if ifDup:
                cur.next = next
            else:
                cur = cur.next
        return dummy.next
