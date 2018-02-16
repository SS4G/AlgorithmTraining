from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        i = 0
        ptr = dummy
        pre_m = None
        pre_n = None
        post_n = None
        while ptr is not None:
            if i == m - 1:
                pre_m = ptr
            elif i == n:
                pre_n = ptr
            ptr = ptr.next
            i += 1
        post_n = pre_n.next
        pre_n.next = None
        head_n, tail_n = self.reverseLinklist(pre_m.next)
        pre_m.next = head_n
        tail_n.next = post_n
        return dummy.next

    def reverseLinklist(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        tailDummy = ListNode(-1)
        ptr = dummy.next
        pos = 0
        ptrNext = None
        while ptr is not None:
            ptrNext = ptr.next
            ptr.next = tailDummy.next
            tailDummy.next = ptr
            ptr = ptrNext
        return tailDummy.next, dummy.next

if __name__ == "__main__":
    s = Solution()
    head = LinkedListUtil.genList([1, 2, 3, 4, 5, 6, 7, 8])
    LinkedListUtil.showList(s.reverseBetween(head, 2, 4))
