class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColour = image[sr][sc]
        addedSet = set([])
        fifo = [(sr, sc), ]
        addedSet.add((sr, sc))
        rd = 0
        while rd < len(fifo):
            curNode = fifo[rd]
            for adjNode in self.getAdj(len(image), len(image[0]), curNode[0], curNode[1]):
                if image[adjNode[0]][adjNode[1]] == oldColour and adjNode not in addedSet:
                    fifo.append(adjNode)
                    addedSet.add(adjNode)
            rd += 1
        for point in fifo:
            image[point[0]][point[1]] = newColor
        return image

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
    imag = [[1,1,1],[1,1,0],[1,0,1]]
    i = s.floodFill(imag, 1, 1, 2)
    s.show2DArr(i)