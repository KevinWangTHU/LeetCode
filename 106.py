# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def buildTree(inL, inR, poL, poR):
            if poL == poR:
                return TreeNode(postorder[poR])
            if poL > poR:
                return None
            pivot = postorder[poR]
            node = TreeNode(pivot)
            for i in range(inL, inR+1):
                if pivot == inorder[i]:
                    break
            node.left = buildTree(inL, i-1, poL, poL+(i-inL)-1)
            node.right = buildTree(i+1, inR, poL+(i-inL), poR-1)
            return node
        return buildTree(0, len(inorder)-1, 0, len(postorder)-1)
