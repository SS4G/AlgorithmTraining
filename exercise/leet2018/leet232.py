class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackPos = []
        self.stackNeg = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackNeg.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stackPos) > 0:
            return self.stackPos.pop()
        else:
            while len(self.stackNeg) > 1:
                self.stackPos.append(self.stackNeg.pop())
            return self.stackNeg.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stackPos) > 0:
            return self.stackPos[-1]
        else:
            while len(self.stackNeg) > 1:
                self.stackPos.append(self.stackNeg.pop())
            res = self.stackNeg[-1]
            self.stackPos.append(self.stackNeg.pop())
            return res

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stackPos) == 0 and len(self.stackNeg) == 0


        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()