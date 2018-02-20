from AlgorithmTraining.G55Utils.Py.Utils import *
import heapq

class ListHead:
    def __init__(self, node):
        self.val = node.val
        self.head = node

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapq.heapify(heap)
        dummyHead = ListNode(0)
        ptr = dummyHead
        for head in lists:
            if head is not None:
                heapq.heappush(heap, ListHead(head))
        while len(heap) > 0:
            tmpNode = heapq.heappop(heap)
            ptr.next = tmpNode.head
            ptr = ptr.next
            if ptr.next is not None:
                heapq.heappush(heap, ListHead(ptr.next))
        return dummyHead.next

        #
        #


if __name__ == "__main__":
    s = Solution()
    l1 = LinkedListUtil.genList([1, 2, 3, 4, 5])
    l2 = LinkedListUtil.genList([1, 2, 3, 4])
    l3 = LinkedListUtil.genList([1, 2, 3])
    ls = [l1, l2, l3]
    LinkedListUtil.showList(s.mergeKLists(ls))

#li = []
#heapq.heapify(li)
##
#heapq.heappush(li, 2)
#heapq.heappush(li, 5)
#heapq.heappush(li, 4)
#heapq.heappush(li, 1)
#heapq.heappush(li, 0)
#heapq.heappush(li, 8)
##
#print(heapq.heappop(li))
#print('-', len(li))
#print(heapq.heappop(li))
#print('-', len(li))
#print(heapq.heappop(li))
#print('-', len(li))
#print(heapq.heappop(li))
#print('-', len(li))
#print(heapq.heappop(li))
#print('-', len(li))
#print(heapq.heappop(li))

