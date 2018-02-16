from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = self.getLen(headA)
        lb = self.getLen(headB)
        #print(la, lb)
        if la < lb:
            headA, headB = headB, headA
        assert la >= lb, "wtf?"
        ptra = headA
        ptrb = headB
        for i in range(la - lb):
            ptra = ptra.next

        while ptra is not None and ptrb is not None and ptra is not ptrb:
            ptra = ptra.next
            ptrb = ptrb.next

        return ptra

    def getLen(self, head):
        ptr = head
        l = 0
        while ptr is not None:
            ptr = ptr.next
            l += 1
        return l

if __name__ == "__main__":
    la = LinkedListUtil.genList([])
    lb = LinkedListUtil.genList([7])
    #tmpb = lb
    #for i in range(2):
    #    tmpb = tmpb.next
    #tmpb.next = la.next
    #LinkedListUtil.showList(lb)
    s = Solution()
    LinkedListUtil.showList(s.getIntersectionNode(lb, la))