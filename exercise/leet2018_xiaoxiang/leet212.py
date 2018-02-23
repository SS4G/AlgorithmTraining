class TrieNode:
    def __init__(self):
        self.isWord = False
        self.charDict = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for c in word:
            if c not in ptr.charDict:
                ptr.charDict[c] = TrieNode()
            ptr = ptr.charDict[c]
        ptr.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = self.root
        for c in word:
            if c not in ptr.charDict:
                return False
            ptr = ptr.charDict[c]
        return ptr.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.root
        for c in prefix:
            if c not in ptr.charDict:
                return False
            ptr = ptr.charDict[c]
        return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        wordStack = []
        posStack = set()
        output = set()
        rL = len(board)
        if rL == 0:
            return output
        cL = len(board[0])
        for r in range(rL):
            for c in range(cL):
                self.dfsHelper(board, r, c, rL, cL, wordStack, posStack, trie, output)
                if len(output) == len(words):
                    break
        return list(output)

    def dfsHelper(self, board, r, c, rL, cL, wordStack, posStack, trie, output):
        """
        :param board:
        :param r:
        :param c:
        :param rL:
        :param cL:
        :param wordStack:
        :param posStack:
        :param trie: Trie
        :param output: set
        :return:
        """
        wordStack.append(board[r][c])
        posStack.add((r, c))
        if trie.startsWith(wordStack):
            if trie.search(wordStack):
                output.add("".join(wordStack))
            for nr, nc in self.getAdj(rL, cL, r, c):
                if (nr, nc) not in posStack:
                    self.dfsHelper(board, nr, nc, rL, cL, wordStack, posStack, trie, output)
        wordStack.pop()
        posStack.remove((r, c))

    def getAdj(self, rL, cL, r, c):
        adjs = []
        if r < rL - 1:
            adjs.append((r + 1, c))
        if r > 0:
            adjs.append((r - 1, c))
        if c < cL - 1:
            adjs.append((r, c + 1))
        if c > 0:
            adjs.append((r, c - 1))
        return adjs

if __name__ == "__main__":
    s = Solution()
    board = [
      ['o', 'a', 'a', 'n'],
      ['e', 't', 'a', 'e'],
      ['i', 'h', 'k', 'r'],
      ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(s.findWords(board, words))
