class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        rL = len(grid)
        if rL == 0:
            return 0
        cL = len(grid[0])
        marked = [[-1 for i in range(cL)] for i in range(rL)]
        markId = 0
        for r in range(rL):
            for c in range(cL):
                self.dfsHelper(r, c, rL, cL, grid, marked, markId)
                markId += 1

        res = set()
        for r in range(rL):
            for c in range(cL):
                if marked[r][c] >= 0:
                    res.add(marked[r][c])
        return len(res)

    def dfsHelper(self, r, c, rL, cL, grid, marked, markId):
        if marked[r][c] == -1 and grid[r][c] == "1":
            marked[r][c] = markId
            for nr, nc in self.getAdj(rL, cL, r, c):
                self.dfsHelper(nr, nc, rL, cL, grid, marked, markId)

    def getAdj(self, rL, cL, r, c):
        adjs = []
        if r < rL - 1:
            adjs.append((r + 1, c))
        if r > 0:
            adjs.append((r - 1, c))
        if c < cL - 1:
            adjs.append((r, c + 1))
        if c > 0:
            adjs.append((r, c - 1))
        return adjs

if __name__ == "__main__":
    s = Solution()
    grid = [list("11000"),
            list("11000"),
            list("00100"),
            list("00011"),]
    print(s.numIslands(grid))