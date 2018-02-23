class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0, 0] for i in range(len(nums))]  # 0 not rob 1 rob
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = nums[i] + dp[i - 1][0]
        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])