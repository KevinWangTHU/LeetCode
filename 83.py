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
        dummy = ListNode(-9999999)
        dummy.next = head
        prev = dummy.val
        c = dummy
        while c.next:
            c = c.next
            while c.next and c.next.val == c.val:
                c.next = c.next.next
        return dummy.next
