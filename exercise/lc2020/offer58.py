class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        res = n % len(s)
        return s[res: ] + s[: res]
