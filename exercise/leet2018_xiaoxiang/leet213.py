class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0, 0] for i in range(len(nums))]  # 0 not rob 1 rob
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, len(nums) - 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = nums[i] + dp[i - 1][0]
        st1 = max(dp[len(nums) - 2][0], dp[len(nums) - 2][1])
        # not rob n-1

        dp = [[0, 0] for i in range(len(nums))]  # 0 not rob 1 rob
        dp[1][0] = 0
        dp[1][1] = nums[1]
        for i in range(2, len(nums) - 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = nums[i] + dp[i - 1][0]
        st2 = max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])
        # not rob 0

        return max(st1, st2)