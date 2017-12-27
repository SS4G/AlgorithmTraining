class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return

    def matchFirst(self, s, p):
        sIdx = 0
        pIdx = 0
        while sIdx < len(s) and pIdx < len(p):
            if pIdx < len(p) - 1 and p[pIdx + 1] == '*':
                if p[pIdx] == '.':  # .* found
                    for stIdx in range(sIdx, len(s)):
                        if self.matchFirst(s[stIdx:], p[pIdx + 2:]):
                            return True
                    return False
                else:  # a*found
                    sameIdx = sIdx
                    while sameIdx < len(s) and s[sameIdx] == s[sIdx]:
                        sameIdx += 1
                    for stIdx in range(max(sIdx - 1, 0), sameIdx):
                        if self.matchFirst(s[stIdx:], p[pIdx + 2:]):
                            return True
                    return False
            elif s[sIdx] == p[pIdx] or s[sIdx] == '.':
                sIdx += 1
                pIdx += 1
            else:
                break

        return sIdx == len(s) and pIdx == len(p)