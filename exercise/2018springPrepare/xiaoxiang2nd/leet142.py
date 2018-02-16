from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return None
        if head.next.next is None:
            return None
        fast = head.next.next
        slow = head.next
        while fast is not slow:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            slow = slow.next
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return slow
