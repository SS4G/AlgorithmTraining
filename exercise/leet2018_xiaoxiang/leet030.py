from collections import defaultdict
from copy import deepcopy


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words[0])
        wordsDict = {}
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 0
            wordsDict[word] += 1
        result = []

        #print(wordsDict)

        #for offset in range(n):
        for offset in range(n):
        #for offset in range(1):
            tmpWordsDict = deepcopy(wordsDict)  # copy the dict
            for i in range(offset, min(offset + n * len(words), len(s) - (len(s) % n)), n):  # add first n words
                #print("i=", i)
                getWord = s[i: i + n]
                if getWord in wordsDict:
                    tmpWordsDict[getWord] -= 1
                if self.checkAllZero(tmpWordsDict):
                    result.append(offset)

            for i in range(offset + n * len(words), len(s) - (len(s) % n), n):
                getWord = s[i: i + n]
                removeIdx = i - len(words) * n
                removeWord = s[removeIdx: removeIdx + n]
                if getWord in wordsDict:
                    tmpWordsDict[getWord] -= 1
                if removeWord in wordsDict:
                    tmpWordsDict[removeWord] += 1
                if self.checkAllZero(tmpWordsDict):
                    result.append(removeIdx + n)
        return result

    def checkAllZero(self, dict0):
        for k in dict0:
            if dict0[k] != 0:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    s0 = "barfoothekfoobarmani"
    words = ["foo", "bar"]
    print(s.findSubstring(s0, words))