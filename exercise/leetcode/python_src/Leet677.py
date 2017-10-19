class TrieNode:
    def __init__(self):
        self.charDict = {}
        self.wordMark = False

class TrieUtil:
    @staticmethod
    def insertWord(word, trieRoot):
        ptr = trieRoot
        for c in word:
            if c not in ptr.charDict:
                ptr.charDict[c] = TrieNode()
            ptr = ptr.charDict[c]
        ptr.wordMark = True

    @staticmethod
    def getByPrefix(prefix, trieRoot):
        """
        :param porfix: 
        :param trieRoot: 
        :return: list
        """
        ptr = trieRoot
        for c in prefix:
            if c in trieRoot.charDict:
                ptr = trieRoot.charDict[c]
        output = []
        stack = list(prefix)
        TrieUtil.getPrifixRecure(stack, ptr, output)

    @staticmethod
    def getPrifixRecure(stack, trieRoot, output):
        """        
        :param prefix: 
        :param trieRoot: 
        :return: 
        """
        if trieRoot.wordMark is True:
            output.append("".join(stack))
        if len(trieRoot.charDict) == 0:
            return
        else:
            for c in trieRoot.charDict:
                stack.append(c)
                TrieUtil.getPrifixRecure(stack, trieRoot.charDict[c], output)
                stack.pop()

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valueDict = {}


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.valueDict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sums = 0
        for k in self.valueDict:
            if len(k) >= len(prefix) and k[:len(prefix)] == prefix:
                sums += self.valueDict[prefix]
        return sums

        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)

if __name__ == "__main__":
    print(sorted(reversed(["a", "ap", "app", "apple"])))
    #print("ap" < "app")
    root = TrieNode()
    TrieUtil.insertWord("a", root)
    TrieUtil.insertWord("ap", root)
    TrieUtil.insertWord("app", root)
    TrieUtil.insertWord("apo", root)
    TrieUtil.insertWord("apii", root)
    TrieUtil.insertWord("appple", root)
    TrieUtil.insertWord("appple_watch", root)
    TrieUtil.insertWord("bppple_watch", root)
    print(TrieUtil.getByPrefix("ap", root))