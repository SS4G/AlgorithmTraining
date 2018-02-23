class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        assert len(nums) <= 32
        nums.sort()
        result = []
        for i in range(0x01 << len(nums)):
            result.append(self.mapto(nums, i))
        return result

    def mapto(self, nums, mask):
        result = []
        for i in range(len(nums)):
            if mask & (0x01 << i) != 0:
                result.append(nums[i])
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))