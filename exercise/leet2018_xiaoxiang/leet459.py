class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if len(s) <= 1:
            return False
        for i in range(1, len(s)):
            if length % i == 0:
                #print(i)
                if s == (s[:i] * (length // i)):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    assert s.repeatedSubstringPattern("abab")
    assert s.repeatedSubstringPattern("abcabc")