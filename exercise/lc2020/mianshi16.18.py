from collections import Counter
class Solution(object):
    def checkPattern(self, aLength, bLength, pattern, value):
        if aLength == 0:
            segLength = len(value) / bLength
            patternValue = None
            for i in range(i, len(value), segLength):
                if i == 0:
                    patternValue = pattern[i: i + segLength]
                else:
                    if patternValue != pattern[i: i + segLength]:
                        return False
            return True
        else:
            patDict = {}
            lengthDict = {}
            idx = 0
            for patChar in pattern:
                if patChar == 'a' and 'a' not in patDict:
                    patDict['a'] = value[idx: idx + aLength]
                    lengthDict['a'] = aLength
                    idx += aLength
                elif patChar == 'b' and 'b' not in patDict:
                    patDict['b'] = value[idx: idx + bLength]
                    lengthDict['b'] = bLength
                    idx += bLength
                else:


    def patternMatching(self, pattern, value):
        """
        :type pattern: str
        :type value: str
        :rtype: bool
        """
        patternCounter = Counter(pattern)
        valueLength = len(value)
        if a not in 

        for aLength in range(valueLength):
            if 'a' not in patternCounter['a']:

            if
            