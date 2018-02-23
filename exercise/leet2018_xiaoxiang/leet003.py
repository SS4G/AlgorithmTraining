class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        repeatSet = set([])
        rd = 0
        wr = 0
        maxLen = 0
        while True:
            if wr < len(s) and s[wr] not in repeatSet:
                repeatSet.add(s[wr])
                wr += 1
                maxLen = max(maxLen, wr - rd)
            elif wr == len(s):
                break
            elif s[rd] in repeatSet:
                repeatSet.remove(s[rd])
                rd += 1
            else:
                print(repeatSet, rd)
        return maxLen

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))