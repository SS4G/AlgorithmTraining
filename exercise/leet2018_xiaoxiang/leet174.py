class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rowLen = len(dungeon)
        colLen = len(dungeon[0])
        dp = [[-1, ] * colLen for i in range(rowLen)]
        dp[rowLen - 1][colLen - 1] = -(dungeon[rowLen - 1][colLen - 1])
        dp[rowLen - 1][colLen - 1] = 0 if dp[rowLen - 1][colLen - 1] < 0 else dp[rowLen - 1][colLen - 1]
        #print(dp)
        for i in reversed(range(0, rowLen - 1)):
            dp[i][colLen - 1] = dp[i + 1][colLen - 1] - dungeon[i][colLen - 1]
            dp[i][colLen - 1] = 0 if dp[i][colLen - 1] < 0 else dp[i][colLen - 1]
        #print(dp)
        for j in reversed(range(0, colLen - 1)):
            dp[rowLen - 1][j] = dp[rowLen - 1][j + 1] - dungeon[rowLen - 1][j]
            dp[rowLen - 1][j] = 0 if dp[rowLen - 1][j] < 0 else dp[rowLen - 1][j]

        #print(dp)

        for r in reversed(range(0, rowLen - 1)):
            for c in reversed(range(0, colLen - 1)):
                dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = 0 if dp[r][c] < 0 else dp[r][c]
        if dp[0][0] < 0:
            return 1
        return dp[0][0] + 1

if __name__ == "__main__":
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    dungeon = [[-3, 5]]
    s = Solution()
    print(s.calculateMinimumHP(dungeon))