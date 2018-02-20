import heapq
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        li = [i for i in zip(Profits, Capital)]
        li.sort(key=lambda x: (x[1], -x[0]))  # 按照启动资本从小到达排序
        heap = []
        heapq.heapify(heap)
        curCaptal = W
        ptr = 0
        for i in range(k):
            while ptr < len(Profits) and li[ptr][1] <= curCaptal:
                heapq.heappush(heap, (-li[ptr][0], li[ptr][1]))  # 将可以启动的项目放入堆中
                ptr += 1
            if len(heap) > 0:
                curCaptal += (-heapq.heappop(heap)[0])
        return curCaptal

if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3]
    b = [0, 1, 1]
    print(s.findMaximizedCapital(2, 0, a, b))
    print([x for x in zip(a, b)])