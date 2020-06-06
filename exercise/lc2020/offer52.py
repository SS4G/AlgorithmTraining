from G55Utils.Py.Utils import ListNode
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA = headA
        ptrB = headB
        cntA = 0
        while ptrA is not None:
            cntA += 1
            ptrA = ptrA.next

        cntB = 0
        while ptrB is not None:
            cntB += 1
            ptrB = ptrB.next
        
        longgerHead = None
        shorterHead = None
        if cntA >= cntB:
            longgerHead = headA
            shorterHead = headB
        else:
            longgerHead = headB
            shorterHead = headA
        
        diffLength = abs(cntA - cntB)
        longgerPtr = longgerHead
        shorterPtr = shorterHead
        for i in range(diffLength):
            longgerPtr = longgerPtr.next
        
        while longgerPtr != shorterPtr and longgerPtr is not None:
            longgerPtr = longgerPtr.next
            shorterPtr = shorterPtr.next

        return longgerPtr




        