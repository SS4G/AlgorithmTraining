from collections import defaultdict
from itertools import product

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matchedDict = defaultdict(dict)
        p = self.zipPattern(p)
        dp = [[False, ] * len(p) for i in range(len(s))]
        for i in range(len(s)):
            if p[0] == "*" or p[0] == "?":
                dp[i][0] = True
            elif i == 0 and p[0] == s[0]:
                dp[i][0] = True
            else:
                dp[i][0] = False

        for j in range(1, len(p)):
            if p[j] == "*" or p[j] == "?":
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = p[j - 1] == "*" and s[0] == p[j] and dp[0][j - 1]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] == "*":
                    dp[i][j] = dp[i - 1][j]
                elif p[j] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i] == p[j]

        #print(dp)

        return dp[len(s) - 1][len(p) - 1]

    def zipPattern(self, s):
        patternBuffer = []
        for c in s:
            if len(patternBuffer) > 0 and c == "*" and patternBuffer[-1] == "*":
                continue
            else:
                patternBuffer.append(c)
        return "".join(patternBuffer)


if __name__ == "__main__":
    s = Solution()
    cases = [
        ("aa", "a", False), 
        ("aa", "*", True), 
        ("cb", "?a", False), 
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
        ("aab", "c*a*b", False),
        ("ho", "**ho", True),
        ("abababaabaabbaaababaaabbaabbababaaabbababbbabaaaaabaaababbbbabaabbbabaaabaaaabbababbaabbbabbbbaaabaaaaababaaabbbbaababbabababbaabaabaaabbabbbaaaaaabbbbabaaaaaabaaabbaaabbaaaababbbaaabbbbbbaaaaaabbababbaa", "b**b*ab***bb**ab**bb*baa**abb*b*ba*aaa**a****aaa*bbb***ba**bba**a**b*b**a*b**b*b*a***b***b*ab***bb*a****", False)
        ]

    for case in cases:
        try:
            assert s.isMatch(case[0], case[1]) == case[2]
        except AssertionError as e:
            print(case)

