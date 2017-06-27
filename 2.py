# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        carry = 0
        while l1 or l2 or carry:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            cur_num = a + b + carry
            cur_num, carry = cur_num % 10, cur_num / 10
            cur = ListNode(cur_num)
            head.next = cur
            head = cur
        return dummy.next
