# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from AlgorithmTraining.G55Utils.Py.Utils import *

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        else:
            res = head.next  # return p2
            ptr = head
            while ptr is not None:
                ptr = self.swap4Node(ptr)

        return res

    def swap4Node(self, head):
        p1, p2, p3, p4 = None, None, None, None
        p1 = head
        if head is not None:
            p1 = head
            if head.next is not None:
                p2 = head.next
                if head.next.next is not None:
                    p3 = head.next.next
                    if head.next.next.next is not None:
                        p4 = head.next.next.next

        if p2 is None:
            return None
        elif p2 is not None and p4 is not None:
            p2.next = p1
            p1.next = p4
            return p3
        elif p2 is not None and p4 is None:
            p2.next = p1
            p1.next = p3
            return p3


if __name__ == "__main__":
    s = Solution()
    l = LinkedListUtil.genList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    h = s.swapPairs(l)
    LinkedListUtil.showList(h)