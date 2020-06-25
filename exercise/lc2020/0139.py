from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        failedRecordDict = defaultdict(lambda :defaultdict(lambda :True))
        return self.wordBreakHelper(s, wordDict, failedRecordDict)

    def wordBreakHelper(self, s, wordDict, failedRecordDict):
        if len(s) == 0:
            return True
        for word in wordDict:
            if not failedRecordDict[s][word]:
                return False
            if s.startswith(word):
                res = self.wordBreakHelper(s[len(word):], wordDict, failedRecordDict)
                if res == True:
                    return True
                else:
                    failedRecordDict[s][word] = False
        return False

if __name__ == "__main__":
    s = Solution()
    str0 = "cars"
    wordList = ["car", "ca", "rs"]
    assert s.wordBreak(str0, wordList)
