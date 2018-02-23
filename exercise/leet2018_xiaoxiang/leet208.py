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

