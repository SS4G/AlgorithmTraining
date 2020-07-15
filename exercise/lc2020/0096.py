class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dps = [None, ] * (4 + n + 1)
        dps[0] = 1
        dps[1] = 1
        dps[2] = 2
        dps[3] = 5
        if n <= 3:
            return dps[n]
        else:
            for i in range(4, n):
                dps[n] = sum([dps[left] * dps[n - 1 - left] for left in range(n)])
        return dps[n]

