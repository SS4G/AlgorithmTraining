class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dps = []
        for r in triangle:
            dps.append([0xffffffff,] * len(r))
        dps[0][0] = triangle[0][0]
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if 0 < c < len(triangle[r]) - 1:
                    dps[r][c] = min(dps[r - 1][c], dps[r - 1][c - 1]) + triangle[r][c]
                elif c == 0:
                    dps[r][c] = dps[r - 1][c] + triangle[r][c]
                else:
                    dps[r][c] = dps[r - 1][c - 1] + triangle[r][c]
        return min(dps[-1])
