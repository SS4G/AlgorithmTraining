class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s = num
        for i in range(k):
            s = self.remove1digit(s)
            #print(s)
        return s

    def remove1digit(self, s):
        if len(s) == 1:
            return '0'
        else:
            targetIdx = self.find1stPeek(s)
            tmpStr = s[:targetIdx] + s[targetIdx + 1:]
            i = 0
            while i < len(tmpStr) - 1 and tmpStr[i] == '0':
                i += 1
            return tmpStr[i:]

    def find1stPeek(self, s):
        i = 0
        while i < len(s) - 1:
            if int(s[i]) > int(s[i + 1]):
                return i
            else:
                i += 1
        return len(s) - 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeKdigits("10", 2))