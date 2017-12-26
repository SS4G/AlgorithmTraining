from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degreeSet = set([])
        degreeVal = 0
        cnt = defaultdict(lambda :0)
        for i in nums:
            cnt[i] += 1
        maxVal = max(cnt.values())
        degreeSet = set([k for k in cnt.keys() if cnt[k] == maxVal])
        minLen = 1000000000
        leftIdxs = {}
        rightIdxs = {}
        for i in range(len(nums)):
            if nums[i] in degreeSet:
                if nums[i] not in leftIdxs:
                    leftIdxs[nums[i]] = i

        for c in degreeSet:
            minLen = min(self.findLeftAndRight(nums, c), minLen)
        return minLen

    def findLeftAndRight(self, nums, v):
        leftIdx = 0
        while nums[leftIdx] != v:
            leftIdx += 1
        rightIdx = len(nums) - 1
        while nums[rightIdx] != v:
            rightIdx -= 1
        return rightIdx - leftIdx + 1

if __name__ == "__main__":
    s = Solution()
    print(s.findShortestSubArray([1, 2, 2, 3, 1]))