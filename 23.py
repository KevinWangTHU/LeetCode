# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def up(h):
    i = len(h) - 1
    while i > 0 and h[i].val < h[(i-1)//2].val:
        h[(i-1)//2], h[i] = h[i], h[(i-1)//2]
        i = (i-1) // 2


def down(h):
    i = 0
    while (2*i+1 < len(h)):
        p = i
        if 2*i+2 < len(h):
            l = 2*i+1
            r = 2*i+2
            if h[l].val < h[p].val and h[l].val <= h[r].val:
                h[l], h[p] = h[p], h[l]
                i = 2*i+1
            elif h[r].val < h[p].val and h[r].val <= h[l].val:
                h[r], h[p] = h[p], h[r]
                i = 2*i+2
            else:
                return
        else:
            l = 2*i+1
            if h[l].val < h[p].val:
                h[l], h[p] = h[p], h[l]
                i = 2*i+1
            else:
                return


def push(h, ln):
    h.append(ln)
    up(h)


def pop(h):
    ans = h[0]
    h[0] = h[-1]
    del h[-1]
    down(h)
    return ans


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ansList = ListNode(0)
        tail = ansList
        h = []

        for i in range(len(lists)):
            if lists[i]is not None:
                push(h, lists[i])

        while len(h) > 0:
            p = pop(h)
            tail.next = ListNode(p.val)
            tail = tail.next
            if p.next is not None:
                push(h, p.next)

        return ansList.next
