import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap, -i)
        res = 0
        for i in range(k):
            res = -heapq.heappop(heap)
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 4, 2, 1, 6, 2, 3]
    print(s.findKthLargest(nums, 3))

