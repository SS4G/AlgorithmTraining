## leetcode 126
### solution
通配符建图的方式建图可以有效地减少时间复杂度。单词两两比较建图的方式复杂度为`O(n^2)` 会超时。通配符的方式只需要 将一单词抽象为通配符 同一个通配符下的单词是相邻的 比如 ABC 抽象为 `A*B`, `*BC`, `AB*` 这种方式建图的时间只需要 
`O(n*word_length)`。之后就是使用BFS的过程了。

### code
```Python
from collections import defaultdict
from itertools import combinations
class Solution(object):
    def genMatchCode(self, word):
        """
        生成给定词语的通配符 
        """
        length = len(word)
        for i in range(length):
            yield "{}_{}".format(word[:i], word[i + 1:])

    def buildGraph(self, wordList):
        """
        使用通配符的方式建图 一个通配符下的词语之间有边 可以从O(n^2)降低到O(n)
        """
        matchCodes = defaultdict(set)
        for word in wordList:
            for matchCode in self.genMatchCode(word):
                matchCodes[matchCode].add(word)

        graph = defaultdict(set)
        length = len(wordList)
        for matchCode in matchCodes:
            if len(matchCodes[matchCode]) >= 2:
                for word1, word2 in combinations(matchCodes[matchCode], r=2):
                    graph[word1].add(word2)
                    graph[word2].add(word1)

        return graph

    def genPath(self, tracker, currentWord, currentPath, paths):
        """
        根据追踪字典生成 路径
        currentWord not inserted
        currentPath start from empty
        """
        if len(tracker[currentWord]) == 0:
            currentPath.append(currentWord)
            paths.append(currentPath[:])
            currentPath.pop()
        else:
            currentPath.append(currentWord)
            for prevWord in tracker[currentWord]:
                self.genPath(tracker, prevWord, currentPath, paths)
            currentPath.pop()

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        graph = self.buildGraph(wordList)
        print("graph ready")
        fifo = [beginWord]
        rd = 0
        bfsHistory ={beginWord: 0}
        tracker = defaultdict(set)
        while rd < len(fifo):
            currentWord = fifo[rd]
            if endWord in bfsHistory and bfsHistory[currentWord] >= bfsHistory[endWord]:
                rd += 1
                continue

            for adjWord in graph[currentWord]:
                if adjWord not in bfsHistory or bfsHistory[adjWord] == bfsHistory[currentWord] + 1:
                    tracker[adjWord].add(currentWord)
                    fifo.append(adjWord)
                    bfsHistory[adjWord] = bfsHistory[currentWord] + 1
            rd += 1
        if endWord not in tracker:
            return []
        else:
            paths = []
            self.genPath(tracker, endWord, [], paths)
            for path in paths:
                path.reverse()
            return paths

```