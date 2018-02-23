class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorRes = 0
        for i in nums:
            xorRes ^= i
        mask = 0x01
        for i in range(32):
            if (0x01 << i) & xorRes != 0:
                mask = (0x01 << i)
                break
        posRes = 0
        negRes = 0
        for n in nums:
            if n & mask != 0:
                posRes ^= n
            else:
                negRes ^= n
        print(posRes, negRes)
        return [self.transFormNeg(posRes), self.transFormNeg(negRes)]

    def transFormNeg(self, res):
        if res & (0x01 << 31) != 0:  #  neg
            res = -((0x01 << 32) - res)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([-1, 0]))