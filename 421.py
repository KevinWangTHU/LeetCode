class TreeNode(object):
    def __init__(self):
        self.left = None
        self.right = None

class Solution(object):
    def findMaximumXOR_trie(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TreeNode()
        for n in nums:
            cur = root
            for i in range(31, -1, -1):
                mask = 1 << i
                if n & mask:
                    if not cur.right:
                        cur.right = TreeNode()
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = TreeNode()
                    cur = cur.left
        MAX = 0
        for n in nums:
            cur = root
            curXor = 0
            for i in range(31, -1, -1):
                mask = 1 << i
                curXor <<= 1
                if n & mask and cur.left:
                    curXor += 1
                    cur = cur.left
                elif not n & mask and cur.right:
                    curXor += 1
                    cur = cur.right
                else:
                    cur = cur.left if cur.left else cur.right
            MAX = max(MAX, curXor)
        return MAX
    def findMaximumXOR(self, nums):
        MAX, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for n in nums:
                s.add(n & mask)

            tmp = MAX | (1 << i)
            for prefix in s:
                if (tmp ^ prefix) in s:
                    MAX = tmp
                    break
        return MAX

s=Solution()
print s.findMaximumXOR([3, 10, 5, 25, 2, 8])
