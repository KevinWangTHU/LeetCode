class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.stemp = []
        self.first = None


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s.append(x)
        self.first = self.first or x


    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.s)):
            self.stemp.append(self.s.pop())
        ret = self.stemp.pop()
        self.first = None if len(self.stemp) == 0 else self.stemp[-1]
        for i in range(len(self.stemp)):
            self.s.append(self.stemp.pop())
        return ret

    def peek(self):
        """
        :rtype: int
        """
        return self.first


    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.s) == 0 else False

s=Queue()
s.push(1)
s.push(2)
print s.peek()
print s.pop()
print s.peek()
print s.pop()
print s.empty()
print s.peek()
