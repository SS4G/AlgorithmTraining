## leetcode 139
### solution
需要一个字典记录下在哪个子字符串下之前失败过 这样可以实现剪枝 避免重复查找

### code
```Python
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
```