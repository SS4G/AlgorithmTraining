from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cntDict = defaultdict(lambda: 0)
        for i in t:
            cntDict[i] += 1
        wr = 0
        rd = 0
        window = s * 2
        # print(cntDict)
        while rd < len(s):
            allZero = self.checkAllZero(cntDict)
            if wr < len(s) and not allZero:
                cntDict[s[wr]] -= 1
                wr += 1
            elif allZero:
                if len(window) > wr - rd:
                    window = s[rd: wr]
                cntDict[s[rd]] += 1
                rd += 1
            else:
                cntDict[s[rd]] += 1
                rd += 1
        return window if len(window) != 2 * len(s) else ""

    def checkAllZero(self, dict0):
        for k in dict0:
            if dict0[k] > 0:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "AABC"))
