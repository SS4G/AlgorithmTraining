class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        RL = len(dungeon)
        CL = len(dungeon[0])
        hps = [[None,] * CL for i in range(RL)]
        for r in range(RL - 1, -1, -1):
            for c in range(CL - 1, -1, -1):
                if r == RL - 1 and c == CL - 1:
                    if dungeon[r][c] >= 0:
                        hps[r][c] = 1
                    else:
                        hps[r][c] = -dungeon[r][c] + 1
                elif r == RL - 1:
                    if dungeon[r][c] >= 0:
                        hps[r][c] = max(1, hps[r][c + 1] - dungeon[r][c])
                    else:
                        hps[r][c] = hps[r][c + 1] + abs(dungeon[r][c])
                elif c == CL - 1:
                    if dungeon[r][c] >= 0:
                        hps[r][c] = max(1, hps[r + 1][c] - dungeon[r][c])
                    else:
                        hps[r][c] = hps[r + 1][c] + abs(dungeon[r][c])
                else:
                    if dungeon[r][c] >= 0:
                        hps[r][c] = max(1, min(hps[r + 1][c], hps[r][c + 1]) - dungeon[r][c])
                    else:
                        hps[r][c] = min(hps[r + 1][c], hps[r][c + 1]) + abs(dungeon[r][c])
        #print(hps)
        return hps[0][0]

if __name__ == "__main__":
    s = Solution()
    assert s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7