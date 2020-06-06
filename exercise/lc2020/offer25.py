from G55Utils.Py.Utils import ListNode
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp1 = l1
        tmp2 = l2
        resultHead = ListNode(None)
        result = resultHead
        while tmp1 is not None and tmp2 is not None:
            if tmp1.val <= tmp2.val:
                result.next = tmp1
                tmp1 = tmp1.next
            else:
                result.next = tmp2
                tmp2 = tmp2.next
            result = result.next

        nonEmptyList = tmp2 if tmp1 is None else tmp1
        if nonEmptyList is not None:
            tmp = nonEmptyList
            while tmp is not None:
                result.next = tmp
                result = result.next
                tmp = tmp.next
        return resultHead.next


