class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -0xffffffff
        curSum = 0
        for i in nums:
            curSum += i
            maxSum = max(curSum, maxSum)
            if curSum < 0:
                curSum = 0
        return maxSum