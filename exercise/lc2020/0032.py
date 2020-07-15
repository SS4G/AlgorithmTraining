class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for idx, c in enumerate(s):
            if len(stack) == 0:
                stack.append((c, idx))
            elif c == ')' and stack[-1][0] == '(':
                stack.pop()
            else:
                stack.append((c, idx))

        if len(stack) == 0:
            maxLen = len(s)
        else:
            maxLen = stack[0][1] - 0
            for i in range(1, len(stack)):
                maxLen = max(stack[i][1] - stack[i - 1][1] - 1, maxLen)
            maxLen = max(maxLen, len(s) - stack[-1][1] - 1)

        return maxLen

if __name__ == "__main__":
    s = Solution()
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses(")()()") == 4
    assert s.longestValidParentheses("()()") == 4
    assert s.longestValidParentheses("())") == 2