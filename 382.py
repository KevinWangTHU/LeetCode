# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        while head:
            head = head.next
            self.length += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = self.length - 1
        randnum = randint(0, count)
        ret = self.head
        while randnum and ret.next:
            count -= 1
            ret = ret.next
            randnum = randint(0, count)
        return ret.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
