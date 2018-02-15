from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        ptr1 = l1
        ptr2 = l2
        ptr = dummy
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next

        while ptr1 is not None:
            ptr.next = ptr1
            ptr1 = ptr1.next
            ptr = ptr.next

        while ptr2 is not None:
            ptr.next = ptr1
            ptr1 = ptr1.next
            ptr = ptr.next

        return dummy.next

if __name__ == "__main__":
    s = Solution()
    l1 = LinkedListUtil.genList([1, 2, 3, 4, 5])
    l2 = LinkedListUtil.genList([1, 2, 3, 4])
    LinkedListUtil.showList(s.mergeTwoLists(l1, l2))
