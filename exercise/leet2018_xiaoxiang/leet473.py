from collections import defaultdict


class Solution(object):

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.path = []
        sticks = defaultdict(lambda: 0)
        for i in nums:
            sticks[i] += 1
        #print(sticks)
        sumLen = sum(nums)
        targetSideLen = 0
        if sumLen % 4 != 0:
            return False
        else:
            targetSideLen = sumLen // 4
        #print(targetSideLen)
        return self.dfsHelper(sticks, 0, targetSideLen, 0, 0)

    def dfsHelper(self, sticks, side, targetSideLength, curSideLength, downLimit):
        if side == 4:
            return True
        elif curSideLength > targetSideLength:
            return False
        else:
            res = False
            for stick in sticks:
                if sticks[stick] > 0 and stick >= downLimit:  # from little to big
                    sticks[stick] -= 1
                    self.path.append(stick)
                    #print(self.path)
                    if curSideLength + stick == targetSideLength:
                        res = res or self.dfsHelper(sticks, side + 1, targetSideLength, 0, 0)
                    else:
                        res = res or self.dfsHelper(sticks, side, targetSideLength, curSideLength + stick, stick)
                    self.path.pop()
                    sticks[stick] += 1
            return res


if __name__ == "__main__":
    s = Solution()
    print(s.makesquare([1,2,1,2,3,1,1,1,1,1,1,1,4]))