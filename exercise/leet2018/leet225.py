from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()
        self.storeFlag = True

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.storeFlag:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        
        while len(len(self.queue1))


    def top(self):
        """
        Get the top element.
        :rtype: int
        """


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue2) == 0 and len(self.queue1) == 0


        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()