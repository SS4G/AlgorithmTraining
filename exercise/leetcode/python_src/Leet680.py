class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)
        return self.validPalindromeRecursive(s, start, end, 0)

    def validPalindromeRecursive(self, s, start, end, faild):
        lo = start
        hi = end - 1
        while lo <= hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                if faild > 0:
                    return False
                elif self.validPalindromeRecursive(s, lo + 1, hi + 1, faild + 1) or self.validPalindromeRecursive(s, lo, hi, faild + 1):
                    return True
                else:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("abccba")
    assert s.validPalindrome("abcdcba")
    assert s.validPalindrome("abcdecba")
    assert s.validPalindrome("abcdckba")
    assert not s.validPalindrome("abcedckba")