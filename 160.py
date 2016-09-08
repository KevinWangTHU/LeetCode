class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA
