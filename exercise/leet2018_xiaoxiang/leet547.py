class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        dim = len(M)
        if dim == 0:
            return 0
        record = [i for i in range(dim)]
        for r in range(dim):
            for c in range(r + 1, dim):
                if M[r][c] != 0:
                    self.link(record, r, c)

        return sum([1 if record[i] == i else 0 for i in range(dim)])

    def link(self, record, a, b):
        """
        link a -> b
        :param record:
        :param a:
        :param b:
        :return:
        """
        next = a
        while record[next] != next:
            next = record[next]
        next2 = b
        while record[next2] != next2:
            next2 = record[next2]
        record[next] = next2

if __name__ == "__main__":
    s = Solution()
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    M = [[1,1,0],
         [1,1,1],
         [0,1,1]]
    print(s.findCircleNum(M))
