import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.greaterHeap = [] # add negative integer
        self.smallerHeap = [] # add positive integer
        heapq.heapify(self.greaterHeap)
        heapq.heapify(self.smallerHeap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.smallerHeap, -num)
        if len(self.smallerHeap) - len(self.greaterHeap) >= 2:
            heapq.heappush(self.greaterHeap, -heapq.heappop(self.smallerHeap))
        elif len(self.greaterHeap) > 0 and -self.smallerHeap[0] > self.greaterHeap[0]:
            heapq.heappush(self.greaterHeap, -heapq.heappop(self.smallerHeap))
            heapq.heappush(self.smallerHeap, -heapq.heappop(self.greaterHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smallerHeap) == len(self.greaterHeap):
            greaterNum = heapq.heappop(self.greaterHeap)
            smallerNum = heapq.heappop(self.smallerHeap)

            res = float(greaterNum - smallerNum) / 2
            heapq.heappush(self.greaterHeap, greaterNum)
            heapq.heappush(self.smallerHeap, smallerNum)
            return res
        else:
            midian = heapq.heappop(self.smallerHeap)
            heapq.heappush(self.smallerHeap, midian)
            return float(-midian)


        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()

if __name__ == "__main__":
    m = MedianFinder()
    m.addNum(1)
    m.addNum(2)
    m.addNum(3)
    #m.addNum(3)
    print(m.findMedian())
    m.addNum(5)
    print(m.findMedian())
    heap = [3, 4, 1, 2, 5, 6]
    heapq.heapify(heap)


