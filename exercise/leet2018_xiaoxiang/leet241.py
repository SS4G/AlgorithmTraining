import re

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        pattern = "(\\+|\\-|\\*)"
        pat = re.compile(pattern)
        strings = re.split(pat, input)
        #print(strings)
        res = self.calcRecure(strings)
        res.sort()
        return res

    def calcRecure(self, li):
        if len(li) == 1:
            return [int(li[0]),]
        else:
            res = []
            for i in range(len(li)):
                if i & 0x01 != 0:  # operator
                    leftRes = self.calcRecure(li[:i])
                    rightRes = self.calcRecure(li[i + 1:])
                    for l in leftRes:
                        for r in rightRes:
                            res.append(self.calcValue(l, r, li[i]))
            return res

    def calcValue(self, leftVal, rightVal, op):
        if op == "+":
            return leftVal + rightVal
        elif op == "-":
            return leftVal - rightVal
        else:
            return leftVal * rightVal
if __name__ == "__main__":
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))
    print(s.diffWaysToCompute("2*3-4*5"))