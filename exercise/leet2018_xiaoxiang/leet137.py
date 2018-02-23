class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitCnt = [0, ] * 32
        for i in nums:
            self.countBit(i, bitCnt)
        res = 0
        for i in range(32):
            if bitCnt[i] % 3 == 1:
                res += (0x01 << i)
        if res & (0x01 << 31) != 0:  #  neg
            res = -((0x01 << 32) - res)
        return res

    def countBit(self, num, bitCnt):
        for i in range(32):
            if num & (0x01 << i) != 0:
                bitCnt[i] += 1


def tobits(num):
    str = ""
    for i in range(32):
        if num & (0x01 << i) != 0:
            str = '1' + str
        else:
            str = '0' + str
    print(str)
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2, 5, 1, 2, 1, ]
    assert s.singleNumber(nums) == 5
    print(bin(-4))
    tobits(-1)

