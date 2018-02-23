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
        wr = 0
        rd = 0
        marked = set()
        fifo.append((begin, 1))
        marked.add(begin)
        while rd < len(fifo):
            curWord = fifo[rd][0]
            curDist = fifo[rd][1]
            for adjWord in self.getAdj(curWord, wordSet):
                if adjWord not in marked:
                    fifo.append((adjWord, curDist + 1))
                    marked.add(adjWord)
                    if adjWord == end:
                        return curDist + 1
            rd += 1
        return 0

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
