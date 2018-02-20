class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        lastTmpSpace = triangle[-1][:]
        tmpSpace = [None, ] * len(triangle)
        for i in range(1, len(triangle)):
            rowidx = len(triangle) - 1 - i
            for colIdx in range(len(triangle[rowidx])):
                tmpSpace[colIdx] = triangle[rowidx][colIdx] + min(lastTmpSpace[colIdx], lastTmpSpace[colIdx + 1])
            lastTmpSpace = tmpSpace[:]
        return lastTmpSpace[0]

if __name__ == "__main__":
    s = Solution()
    tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(s.minimumTotal(tri))
