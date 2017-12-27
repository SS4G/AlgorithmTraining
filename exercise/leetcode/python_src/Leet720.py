class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trieRoot = self.buildTrie(words)
        result = []
        stack = []
        self.getCompleteNode(trieRoot, result, stack)
        return result

    def getCompleteNode(self, root, result, stack):
        if len(root.chars) == 0:
            tmpstr = "".join(stack[:])
            if len(result) == 0:
                result.append(tmpstr)
            elif (len(result[0]) < len(tmpstr)) or (len(result[0]) == len(tmpstr) and tmpstr < result[0]):
                result[0] = tmpstr
        else:
            for c in root.chars:
                if root.chars[c].isWord:
                    stack.append(c)
                    self.getCompleteNode(root.chars[c], result, stack)
                    stack.pop()
                else:
                    tmpstr = "".join(stack[:])
                    if len(result) == 0:
                        result.append(tmpstr)
                    elif (len(result[0]) < len(tmpstr)) or (len(result[0]) == len(tmpstr) and tmpstr < result[0]):
                        result[0] = tmpstr

    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            self.insertWord(root, word)
        return root

    def insertWord(self, root, word):
        if len(word) != 0:
            ptr = root
            for c in word:
                if c not in ptr.chars:
                    ptr.chars[c] = TrieNode()
                ptr = ptr.chars[c]
            ptr.isWord = True

if __name__ == "__main__":
    s = Solution()
    l = ["w","wo","wor","worl", "world"]
    l = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(s.longestWord(l))
    assert "ABC" > "AAC"