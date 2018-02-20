class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ratings = [0xffffffff, ] + ratings + [0xffffffff, ]
        print(ratings)
        candys = [0 for i in range(len(ratings))]
        self.fillBottom(ratings, candys)
        print(candys)
        return sum(candys)

    def fillBottom(self, ratings, candys):
        """
        :param ratings:
        :param candys: unfilled value is 0
        :return:
        """
        for i in range(1, len(ratings) - 1):
            if ratings[i - 1] >= ratings[i] <= ratings[i + 1]:
                #  bottom found
                candys[i] = 1
        for i in range(1, len(ratings) - 1):
            if candys[i] == 1:
                leftIdx = i - 1
                rightIdx = i + 1
                while leftIdx > 0 and ratings[leftIdx - 1] >= ratings[leftIdx] > ratings[leftIdx + 1]:
                    candys[leftIdx] = i - leftIdx + 1
                    leftIdx -= 1
                while rightIdx < len(ratings) - 1 and ratings[rightIdx - 1] < ratings[rightIdx] <= ratings[rightIdx + 1]:
                    candys[rightIdx] = rightIdx - i + 1
                    rightIdx += 1

        if candys[1] == 0:
            candys[1] = 1
        if candys[len(ratings) - 2] == 0:
            candys[len(ratings) - 2] = 1

        for i in range(2, len(ratings) - 2):
            if candys[i] == 0:
                if ratings[i - 1] < ratings[i] > ratings[i + 1]:
                    candys[i] = max(candys[i - 1], candys[i + 1]) + 1

if __name__ == "__main__":
    s = Solution()
    ratings = [3, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3]
    print(s.candy(ratings))
