class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentStack = []
        starStack = []
        idx = 0
        for c in s:
            if c == "*":
                starStack.append(idx)
            elif c == "(":
                parentStack.append(idx)
            else:
                if len(parentStack) > 0:
                    parentStack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
                else:
                    return False
            idx += 1
        while len(parentStack) > 0:
            mostRightParent = parentStack.pop()
            if len(starStack) <= 0:
                return False
            mostRightStar = starStack.pop()
            if mostRightParent > mostRightStar:
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    assert s.checkValidString("((()))")
    assert s.checkValidString("(**)))")
    assert s.checkValidString("(**))*))")
    assert s.checkValidString("(**)****)*))")
    assert not s.checkValidString("(((((((((**)*)*))")
    assert not s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")

