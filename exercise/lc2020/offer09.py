class CQueue(object):
    def __init__(self):
        self.append_stack = []
        self.pop_stack = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.append_stack.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if len(self.pop_stack) == 0:
            while len(self.append_stack) > 0:
                self.pop_stack.append(self.append_stack.pop())
        if len(self.pop_stack) > 0:
            return self.pop_stack.pop()
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()