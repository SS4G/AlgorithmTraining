from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        tailDummy = ListNode(-1)
        ptr = dummy.next
        while ptr is not None:
            ptrNext = ptr.next
            ptr.next = tailDummy.next
            tailDummy.next = ptr
            ptr = ptrNext
        return tailDummy.next