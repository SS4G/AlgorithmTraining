class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idxa = len(a) - 1
        idxb = len(b) - 1
        carry = 0
        result = []
        while idxa >= 0 and idxb >= 0:
            thisSum = int(a[idxa]) + int(b[idxb]) + carry
            thisBit = thisSum % 2 
            carry = thisSum // 2
            result.append(thisBit)
            idxa -= 1
            idxb -= 1
        
        while idxa >= 0:
            thisSum = int(a[idxa]) + carry
            thisBit = thisSum % 2 
            carry = thisSum // 2
            result.append(thisBit)
            idxa -= 1

        while idxb >= 0:
            thisSum = int(b[idxb]) + carry
            thisBit = thisSum % 2
            carry = thisSum // 2
            result.append(thisBit)
            idxb -= 1

        if carry > 0:
            result.append(carry)

        return "".join(map(str, reversed(result)))

if __name__ == "__main__":
    s = Solution()
    a = "11"
    b = "1"
    a = "1010"
    b = "1011"
    #assert s.addBinary(a, b) == "100"
    assert s.addBinary(a, b) == "10101"