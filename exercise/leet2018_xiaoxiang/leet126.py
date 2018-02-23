from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
        return self.bfsHelper(wordSet, beginWord, endWord)

    def bfsHelper(self, wordSet, begin, end):
        fifo = []
        rd = 0
        marked = set()
        fifo.append((begin, 1))
        marked.add(begin)
        foundDist = 0xffffffff
        lastDict = defaultdict(list)
        while rd < len(fifo):
            curWord = fifo[rd][0]
            curDist = fifo[rd][1]
            for adjWord in self.getAdj(curWord, wordSet):
                if adjWord not in marked:
                    fifo.append((adjWord, curDist + 1))
                    marked.add(adjWord)
                    print("cur", curWord, "adj", adjWord)
                    lastDict[adjWord].append(curWord)
                    if adjWord == end:
                        foundDist = curDist + 1
            if foundDist < curDist + 1:
                break
            rd += 1
        print(fifo)
        print(lastDict)
        paths = self.dirive(lastDict, end, begin, foundDist)
        return paths

    def dirive(self, lastDict, endWord, begineWord, dist):
        # print("dist", dist)
        paths = [[endWord, ], ]
        # print(len(paths[0]))
        while len(paths[0]) != dist:
            # print(paths)
            tmpPaths = []
            for path in paths:
                # print("dd", path)
                for lastWord in lastDict[path[-1]]:
                    tmpPath = path[:]
                    tmpPath.append(lastWord)
                    tmpPaths.append(tmpPath)
            paths = tmpPaths
            # print(paths)
        return paths

    def getAdj(self, word, wordSet):
        adjs = []
        letterSet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for c in letterSet:
                if c != word[i]:
                    tmpWord = "".join([word[:i], c, word[i + 1:]])
                    if tmpWord in wordSet:
                        adjs.append(tmpWord)
        return adjs

if __name__ == "__main__":
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(s.ladderLength(beginWord, endWord, wordList))