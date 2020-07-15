class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        RL = len(obstacleGrid)
        CL = len(obstacleGrid[0])
        dp = [[0, ] * CL for i in range(RL)]
        dp[0][0] = 1
        for r in range(RL):
            for c in range(CL):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    if obstacleGrid[r][c] == 1:
                        dp[r][c] = 0
                    else:
                        dp[r][c] = dp[r][c - 1]
                elif c == 0:
                    if obstacleGrid[r][c] == 1:
                        dp[r][c] = 0
                    else:
                        dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[RL - 1][CL - 1]

if __name__ == "__main__":
    s 