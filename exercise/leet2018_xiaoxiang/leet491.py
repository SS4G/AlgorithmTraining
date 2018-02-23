class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curArr = set()
        curArr.add(())
        for i in nums:
            tmpArr = []
            for arr in curArr:
                if len(arr) == 0 or i >= arr[-1]:
                    tmpList = list(arr)
                    tmpList.append(i)
                    tmpArr.append(tuple(tmpList))
            for t in tmpArr:
                curArr.add(t)
        return [list(t) for t in curArr if len(t) > 1]


if __name__ == "__main__":
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))


