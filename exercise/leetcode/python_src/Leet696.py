class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        accum = 0
        for i in range(len(s) - 1):
            accum += self.findMaxChange(s, i)
        return accum

    def findMaxChange(self, s, idx):
        if s[idx] != s[idx + 1]:
            leftBit = s[idx]
            rightBit = s[idx + 1]
            left = idx
            right = idx + 1
            while left >= 0 and s[left] == leftBit:
                left -= 1

            while  right < len(s) and s[right] == rightBit:
                right += 1

            return min(idx - left, right - (idx + 1))
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    assert s.countBinarySubstrings("00110011") == 6, "WA"
    assert s.countBinarySubstrings("10101") == 4, "WA"