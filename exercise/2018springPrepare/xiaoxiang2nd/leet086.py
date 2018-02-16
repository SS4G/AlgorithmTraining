from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_lt = ListNode(-1)
        dummy_ge = ListNode(-1)
        ptr_lt = dummy_lt
        ptr_ge = dummy_ge
        ptr = head
        while ptr is not None:
            if ptr.val < x:
                ptr_lt.next = ptr
                ptr_lt = ptr_lt.next
            else:
                ptr_ge.next = ptr
                ptr_ge = ptr_ge.next
            #print(ptr.val)
            ptr = ptr.next
        ptr_lt.next = dummy_ge.next
        ptr_ge.next = None
        return dummy_lt.next

if __name__ == "__main__":
    s = Solution()
    l = LinkedListUtil.genList([1,4,3,2,5,2])
    LinkedListUtil.showList(s.partition(l, 3))