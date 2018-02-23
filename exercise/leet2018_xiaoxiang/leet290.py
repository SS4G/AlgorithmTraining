class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patDict = {}
        sDict = {}
        for p, s in zip(list(pattern), str.split()):
            if p not in patDict and s not in sDict:
                patDict[p] = s
                sDict[s] = p
            elif p in patDict and s in sDict and patDict[p] == s and sDict[s] == p:
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog")
    assert not s.wordPattern("aaaa", "dog cat cat dog")
    assert not s.wordPattern("abba", "dog dog dog dog")