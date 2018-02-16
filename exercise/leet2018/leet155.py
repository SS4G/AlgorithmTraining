class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackNormal = []
        self.stackMin = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stackNormal.append(x)
        if len(self.stackMin) == 0 or x < self.stackMin[-1]:
            self.stackMin.append(x)
        else:
            self.stackMin.append(self.stackMin[-1]) # add min element again

    def pop(self):
        """
        :rtype: void
        """
        self.stackMin.pop()
        return self.stackNormal.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stackNormal[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stackMin[-1]


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()