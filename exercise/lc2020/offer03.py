class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setx = set()
        for i in nums:
            if i not in setx:
                setx.add(i)
            else:
                return i