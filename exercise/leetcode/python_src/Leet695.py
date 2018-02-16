class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        markGrid = [[-1, ] * len(grid[0]) for i in range(len(grid))]
        # init mark grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                markGrid[r][c] = 0 if grid[r][c] == 1 else -1

        maxArea = 0
        islandId = 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                thisArea = self.fill(markGrid, grid, r, c, islandId)
                if thisArea > 0:
                    islandId += 1
                    maxArea = max(thisArea, maxArea)
        #self.show2DArr(markGrid, "marked")
        return maxArea

    def fill(self, markGrid, grid, row, col, islandId):
        """
        markGrid == islandId marked land with landId
        markGrid == 0 unmarked land
        markGrid == -1 sea
        """
        if markGrid[row][col] == -1:
            return 0
        elif markGrid[row][col] == 0:
            fifo = [(row, col),]
            markGrid[row][col] = islandId
            rd = 0
            while rd < len(fifo):
                curNode = fifo[rd]
                for adjNode in self.getAdj(len(grid), len(grid[0]), curNode[0], curNode[1]):
                    if markGrid[adjNode[0]][adjNode[1]] == 0:
                        fifo.append(adjNode)
                        markGrid[adjNode[0]][adjNode[1]] = islandId
                rd += 1
            #print(fifo)
            return rd
        else:
            return 0

    def getAdj(self, rowSize, colSize, row, col):
        adj = []
        if row > 0:
            adj.append((row - 1, col))
        if row < rowSize - 1:
            adj.append((row + 1, col))
        if col < colSize - 1:
            adj.append((row, col + 1))
        if col > 0:
            adj.append((row, col - 1))
        return adj

    def show2DArr(self, grid, info=None):
        if info is not None:
            print("-----------" + info + "--------")
        else:
            print("---------------------------")
        for line in grid:
            print(line)
if __name__ == "__main__":
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    #grid = [[1,1,0,0,0],
    #        [1,1,0,0,0],
    #        [0,0,0,1,1],
    #        [0,0,0,1,1]]
    assert s.maxAreaOfIsland(grid) == 6, "area WA"