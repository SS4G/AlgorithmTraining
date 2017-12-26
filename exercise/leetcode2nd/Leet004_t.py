class Solution(object):
    def __init__(self):
        self.checked = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.matchFirst(s, p)

    def matchFirst(self, s, p):
        if (s, p) in self.checked:
            return self.checked[(s, p)]
        sIdx = 0
        pIdx = 0
        if len(s) == 0 and ((self.endWithAllStar(p)) or len(p) == 0):
            self.checked[(s, p)] = True
            return True
        elif len(s) == 0:
            self.checked[(s, p)] = False
            return False
        while sIdx < len(s) and pIdx < len(p):
            if pIdx < len(p) - 1 and p[pIdx + 1] == '*':
                if p[pIdx] == '.':  # .* found
                    if pIdx == len(p) - 2:
                        self.checked[(s, p)] = True
                        return True
                    for stIdx in range(max(sIdx - 1, 0), len(s)):
                        if self.matchFirst(s[stIdx:], p[pIdx + 2:]):
                            self.checked[(s, p)] = True
                            return True
                    return False
                else:  # a*found
                    sameIdx = sIdx
                    while sameIdx < len(s) and s[sameIdx] == p[pIdx]:
                        sameIdx += 1
                    if pIdx == len(p) - 2 and p[pIdx] == s[sIdx] and sameIdx == len(s):
                        self.checked[(s, p)] = True
                        return True
                    for stIdx in range(max(sIdx - 1, 0), min(sameIdx + 1, len(s))):
                        if self.matchFirst(s[stIdx:], p[pIdx + 2:]):
                            self.checked[(s, p)] = True
                            return True
                    self.checked[(s, p)] = False
                    return False
            elif s[sIdx] == p[pIdx] or p[sIdx] == '.':
                sIdx += 1
                pIdx += 1
            else:
                break
        if pIdx < len(p) and self.endWithAllStar(p[pIdx:]):
            self.checked[(s, p)] = True
            return True
        if sIdx == len(s) and pIdx == len(p):
            self.checked[(s, p)] = True
            return True
        else:
            self.checked[(s, p)] = False
            return False

    def endWithAllStar(self, s):
        cnt = 0
        for i in s:
            if i == '*':
                cnt += 1
        return cnt * 2 == len(s)
if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("abcdef", "abcdef")
    assert s.isMatch("abcdef", "ab..ef")
    assert s.isMatch("abef", "ab.*ef")
    assert s.isMatch("abbbbef", "ab.*ef")
    assert s.isMatch("abxxyyydef", "ab.*.*def")
    assert s.isMatch("abiiiioooof", "ab.*ii.*oof")
    assert s.isMatch("", ".*")
    assert s.isMatch("aasdh", ".*.*.*.*")
    assert s.isMatch("a", ".*")
    assert s.isMatch("", ".*.*.*.*")
    assert s.isMatch("aa", "a*")
    assert not s.isMatch("a", "ab.*")
    assert s.isMatch("aab", "c*a*b")
    assert s.isMatch("aab", "a*b")
    assert s.isMatch("a", "ab*")
    assert not s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
    assert s.isMatch("bbab", "b*a*")
    print("123"[3:])