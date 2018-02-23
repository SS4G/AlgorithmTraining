class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xorRes = 0
        for i in nums:
            xorRes = i ^ xorRes
        return xorRes