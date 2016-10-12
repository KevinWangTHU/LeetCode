# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        global plist, qlist
        plist = []
        qlist = []
        def search(root, cur):
            global plist, qlist
            if root == p:
                plist = cur[:]
            if root == q:
                qlist = cur[:]
            if plist and qlist:
                return
            if root.left:
                cur.append(root.left)
                search(root.left, cur)
                cur.pop()
            if root.right:
                cur.append(root.right)
                search(root.right, cur)
                cur.pop()
        search(root, [root])
        ans = None
        for p, q in zip(plist, qlist):
            if p == q:
                ans = p
        return ans
