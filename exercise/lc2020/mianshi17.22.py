from collections import defaultdict
from itertools import combinations
class Solution(object):
    def getWildCard(self, word):
        for i in range(len(word)):
            yield word[:i] + "*" + word[i + 1:]

    def buildGraph(self, wordList):
        wildcardDicts = defaultdict(list)
        for word in wordList:
            for wildCard in self.getWildCard(word):
                wildcardDicts[wildCard].append(word)
        #print(wildcardDicts)

        graph = defaultdict(set)
        for wildCard in wildcardDicts:
            for word1, word2 in combinations(wildcardDicts[wildCard], r=2):
                graph[word1].add(word2)
                graph[word2].add(word1)
        return graph

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[str]
        """
        wordList.append(beginWord)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        existsSet = set()
        graph = self.buildGraph(wordList)
        #print(graph)
        tracker = {}
        fifo = [beginWord, ]
        existsSet.add(beginWord)
        rd = 0
        finishedFlag = False
        while rd < len(fifo):
            currentWord = fifo[rd]
            for adjWord in graph[currentWord]:
                if adjWord not in existsSet:
                    tracker[adjWord] = currentWord
                    fifo.append(adjWord)
                    existsSet.add(adjWord)
                    if adjWord == endWord:
                        finishedFlag = True
                        break
            if finishedFlag:
                break
            rd += 1
        #print(fifo)
        if endWord not in tracker:
            return []
        path = []
        tmpWord = endWord
        while tmpWord != beginWord:
            path.append(tmpWord)
            tmpWord = tracker[tmpWord]
        path.append(beginWord)
        return list(reversed(path))

if __name__ == "__main__":
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = s.findLadders(beginWord, endWord, wordList)
    print(res)

        
