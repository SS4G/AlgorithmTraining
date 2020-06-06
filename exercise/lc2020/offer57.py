class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        leftPtr = 1
        rightPtr = 2
        currentCumSum = 3
        while rightPtr < target:
            #print(currentCumSum, leftPtr, rightPtr)
            if currentCumSum < target:
                rightPtr += 1
                currentCumSum += rightPtr
            elif currentCumSum == target:
                tmpRes = list(range(leftPtr, rightPtr + 1))
                if len(tmpRes) > 1:
                    res.append(tmpRes)
                currentCumSum -= leftPtr
                leftPtr += 1
            else:
                currentCumSum -= leftPtr
                leftPtr += 1
        return res

if __name__ == "__main__":
    s = Solution()
    r = s.findContinuousSequence(9)
    print(r)