from operator import itemgetter
class Solution(object):
    def count1bits(self, n):
        cnt = 0
        for i in range(32):
            masked = (0x01 << i) & n
            if masked != 0:
                cnt += 1
        return cnt

    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return list(map(itemgetter(1), sorted(zip(arr, map(self.count1bits, arr)), key=itemgetter(1, 0))))

