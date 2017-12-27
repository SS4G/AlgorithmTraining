class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = sum(nums)
        accSum = [0, ] * len(nums)
        accSum[0] = nums[0]
        for i in range(1, len(nums)):
            accSum[i] = accSum[i - 1] + nums[i]

        for i in range(len(nums)):
            if accSum[i] - nums[i] == totalSum - accSum[i]:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    nums = [1,]
    print(s.pivotIndex(nums))