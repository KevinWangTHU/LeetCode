class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.head = 0
        self.qtemp = []
        self.headtemp = 0
        self.last = None


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        self.last = x

    def pop(self):
        """
        :rtype: nothing
        """
        for self.head in range(self.head, len(self.q)):
            if self.head != len(self.q) - 1:
                self.last = self.q[self.head]
                self.qtemp.append(self.q[self.head])
            else:
                ret = self.q[self.head]
                self.head += 1

        for self.headtemp in range(self.headtemp, len(self.qtemp)):
            self.q.append(self.qtemp[self.headtemp])
        self.headtemp += 1
        return ret

    def top(self):
        """
        :rtype: int
        """
        return self.last


    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.q) - self.head == 0 else False

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
print s.q, s.head
print s.empty()
print s.pop()
print s.empty()
s.push(100)
print s.top()
