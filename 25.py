# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + self.next.__str__()

# do not understand the assignment mechanism
# need to read some articles
def kreverse(k, head):
    count = k - 1
    anshead = head
    anstail = head
    while head.next is not None and count > 0:
        x = head.next
        head.next = x.next
        x.next = anshead
        anshead = x
        count -= 1
    return anshead, anstail, count


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        anshead, tail, count = kreverse(k, head)
        if count > 0:
            a, b, c = kreverse(k, anshead)
            return a

        while count == 0 and tail.next is not None:
            t1, t2, count = kreverse(k, tail.next)
            tail.next = t1
            taghead = tail
            tagtail = t1
            tail = t2
        if count > 0:
            a,_ , _ = kreverse(k, tagtail)
            taghead.next = a
        return anshead


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
anshead = s.reverseKGroup(l1, 2)
print anshead
