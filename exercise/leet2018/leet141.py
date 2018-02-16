from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast is not None:
            fast = fast.next
            if fast is None:
                return True
            fast = fast.next
            slow = slow.next
            if fast is slow:
                return True
        return False