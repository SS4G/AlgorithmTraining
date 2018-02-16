class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummyHead = RandomListNode(1)
        dummyHead.next = head
        ptr = dummyHead
        while ptr is not None:
            tmpNode = RandomListNode(ptr.label)
            tmpNode.next = ptr.next
            ptr.next = tmpNode
            ptr = ptr.next
