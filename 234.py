# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):  # O(1) space
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def rev(head):
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

        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        cur = head
        i = 0
        p1 = p2 = None
        while cur:
            i += 1
            if i == (l+1)/2:
                cur.next = rev(cur.next)
                p1 = head
                p2 = cur.next
                break
            cur = cur.next
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
