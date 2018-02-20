from collections import defaultdict

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        forbid = defaultdict(set)
        output = []
        stack = []
        self.placeRecure(n, col=0, stack=stack, forbid=forbid, output=output)
        return [self.plot(n, o) for o in output]

    def placeRecure(self, n, col, stack, forbid, output):
        """
        :param col:
        :return:
        """
        if col == n:
            output.append(stack[:])  # save result
        else:
            for row in range(n):
                point = (row, col)
                if not self.isForbidPostion(forbid, point):
                    # print(point)
                    stack.append(point)
                    self.addForbidPostion(forbid, point)
                    self.placeRecure(n, col + 1, stack, forbid, output)
                    self.removeFobidPosition(forbid, point)
                    stack.pop()

    def isForbidPostion(self, forbid, point):
        """
        :param forbid:
        :return: bool
        """
        row = point[0]
        col = point[1]
        # forbid condition
        # row in forbid["row"]
        # col in forbid["col"]
        # row + col in forbid["posDiag"]
        # row - col in forbid["negDiag"]
        return row in forbid["row"] or col in forbid["col"] or row - col in forbid["posDiag"] or row + col in forbid["negDiag"]

    def addForbidPostion(self, forbid, point):
        """
        :param forbid:
        :return:
        """
        row = point[0]
        col = point[1]
        forbid["row"].add(row)
        forbid["col"].add(col)
        forbid["posDiag"].add(row - col)
        forbid["negDiag"].add(row + col)

    def removeFobidPosition(self, forbid, point):
        row = point[0]
        col = point[1]
        forbid["row"].remove(row)
        forbid["col"].remove(col)
        forbid["posDiag"].remove(row - col)
        forbid["negDiag"].remove(row + col)

    def plot(self, n, points):
        plotPaper = [['.'] * n for i in range(n)]
        for point in points:
            row = point[0]
            col = point[1]
            plotPaper[row][col] = 'Q'
        return ["".join(line) for line in plotPaper]

    def testPlot(self, res):
        for r in res:
            for line in r:
                print(line)
            print("-----------------")
if __name__ == "__main__":
    s = Solution()
    s.testPlot(s.solveNQueens(4))

