class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letterDict = {}
        for i in range(len(letters)):
            if letters[i] not in letterDict:
                letterDict[letters[i]] = i

        for c in "abcdefghijklmnopqrstuvwxyz":
            if (ord(c) > ord(target)) and (c in letterDict):
                return c
        return min(list(letterDict))

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = ""
    s = Solution()
    assert s.nextGreatestLetter(letters, "a") == "c"
    assert s.nextGreatestLetter(letters, "c") == "f"
    assert s.nextGreatestLetter(letters, "g") == "j"
    assert s.nextGreatestLetter(letters, "j") == "c"
    assert s.nextGreatestLetter(letters, "k") == "c"
