class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.s = []
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.s else False

    # @return an integer, the next smallest number
    def next(self):
        node = self.s.pop()
        self.pushAll(node.right)
        return node.val

    def pushAll(self, node):
        while node:
            self.s.append(node)
            node = node.left
