class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = [root] if root else []
        while s:
            cur = s.pop()
            ans.append(cur.val)
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)
        return ans[::-1]

    def postorderTraversal_2(self, root):
        ans = []
        s = [(root, False)]

        while s:
            node, visited = s.pop()
            if visited:
                ans.append(node.val)
            else:
                s.append((node, True))
                if node.right:
                    s.append((node.right, False))
                if node.left:
                    s.append((node.left, False))
        return ans
