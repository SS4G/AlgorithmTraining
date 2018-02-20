# Definition for singly-linked list with a random pointer.
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
            tmpRandom = RandomListNode(ptr.label)
            ptrNext = ptr.next
            ptr.next = tmpRandom
            tmpRandom.next = ptrNext
            ptr = ptrNext

        ptr = dummyHead
        while ptr is not None:
            ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        ptr = dummyHead
        newDummy = RandomListNode(1)
        ptr1New = newDummy
        while ptr is not None:
            tmpNext = ptr.next.next # next node0
            ptr1New.next = ptr.next
            ptr1New = ptr1New.next
            ptr = tmpNext
        return ptr1New.next.next
            #ptr1 =
            #ptr.next = ptrNext




