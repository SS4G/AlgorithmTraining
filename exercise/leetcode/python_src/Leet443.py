class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append(chr(0))
        wr = 0
        rd = 0
        curChar = ""
        curCnt = 0
        while rd < len(chars):
            if curChar != chars[rd]:
                if len(curChar) > 0:
                    chars[wr] = curChar
                    wr += 1
                    if curCnt > 1:
                        for c in str(curCnt):
                            chars[wr] = c
                            wr += 1
                curChar = chars[rd]
                curCnt = 1
            else:
                curCnt += 1
            rd += 1
        return wr

if __name__ == "__main__":
    s = Solution()
    x = ["a"]
    wr = s.compress(x)
    print(x, wr)
