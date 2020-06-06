from G55Utils.Py.Utils import ListNode
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headnode = ListNode(None)
        tmpPtr = head
        while tmpPtr is not None:
            splitNode = tmpPtr
            tmpPtr = tmpPtr.next
            if headnode.next is None:
                headnode.next = splitNode
                splitNode.next = None
            else:
                splitNode.next = headnode.next
                headnode.next = splitNode
        return headnode.next


