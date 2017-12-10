class BiDirectionNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.biLinkListDummy = BiDirectionNode(0)
        self.keyDict = {}
        self.tail = self.biLinkListDummy
        for i in range(capacity):
            self.insertNode(self.biLinkListDummy, BiDirectionNode(-(i + 1)))
        while self.tail.next is not None:
            self.tail = self.tail.next

    def insertNode(self, preNode, newNode):
        newNode.next = preNode.next
        newNode.pre = preNode
        newNode.next.pre = newNode
        preNode.next = newNode

    def removeNode(self, nodeToBeRemoved):
        nodeToBeRemoved.pre.next = nodeToBeRemoved.next
        nodeToBeRemoved.next.pre = nodeToBeRemoved.pre

    def get(self, key):
        """
        :rtype: int
        :type key: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.keyDict:
            self.removeNode(self.keyDict[key])
            self.insertNode(self.biLinkListDummy, BiDirectionNode(key, value))
        else:





        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)