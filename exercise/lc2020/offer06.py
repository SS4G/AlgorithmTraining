# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ptr = head
        res = []
        while ptr is not None:
            res.append(ptr.val)
            ptr = ptr.next
        return res[::-1]
