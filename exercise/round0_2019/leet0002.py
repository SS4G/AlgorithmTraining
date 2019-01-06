# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(None)
        curPtr = head
        thisSum = 0
        carry = 0
        while l1 is not None and l2 is not None:
            tmpVal = l1.val + l2.val + carry
            thisSum = tmpVal % 10
            carry = tmpVal // 10
            curPtr.next = ListNode(thisSum)
            curPtr = curPtr.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            tmpVal = l1.val + carry
            thisSum = tmpVal % 10
            carry = tmpVal // 10
            curPtr.next = ListNode(thisSum)
            curPtr = curPtr.next
            l1 = l1.next

        while l2 is not None:
            tmpVal = l2.val + carry
            thisSum = tmpVal % 10
            carry = tmpVal // 10
            curPtr.next = ListNode(thisSum)
            curPtr = curPtr.next
            l2 = l2.next

        if carry != 0:
            curPtr.next = ListNode(carry)

        return head.next