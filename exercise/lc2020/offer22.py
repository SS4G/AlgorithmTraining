# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        zero = ListNode(None)  
        zero.next = head
        ptr0 = zero
        for i in range(k):
            ptr0 = ptr0.next

        ptr1 = zero
        while ptr0 is not None:
            ptr1 = ptr1.next
            ptr0 = ptr0.next

        return ptr1

