class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minstack or self.minstack and x <= self.minstack[-1]:
            self.minstack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if self.minstack[-1] == x:
            self.minstack.pop()
        return x


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print obj.minstack
print obj.getMin()
print obj.pop()
print obj.getMin()
