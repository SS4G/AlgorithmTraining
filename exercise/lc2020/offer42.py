class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cumSum = [0,] * len(nums)
        for idx, n in enumerate(nums):
            if idx > 0:
                cumSum[idx] = cumSum[idx - 1] + n
            else:
                cumSum[0] = n
        return max(cumSum) - min(cumSum)