# 他的写法很漂亮，注意借鉴。
# 1 - 用dummy处理开头
# 2 - 用or处理结尾

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists_slow_complex(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1

        if l1.val < l2.val:
            h = l1
            l1 = l1.next
        else:
            h = l2
            l2 = l2.next
        c = h
        while not (l1 is None or l2 is None):
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        if l1 is not None:
            c.next = l1
        elif l2 is not None:
            c.next = l2
        return h

    def mergeTwoLists(self, l1, l2):
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next
