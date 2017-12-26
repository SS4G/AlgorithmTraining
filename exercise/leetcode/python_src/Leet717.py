class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        elif bits[-2] == 0 and bits[-1] == 0:
            return True
        else:
            idx = 0
            flag = True
            while idx < len(bits):
                if bits[idx] == 0:
                    idx += 1
                    flag = True
                else:
                    idx += 2
                    flag = False
            return flag


if __name__ == "__main__":
    s = Solution()
    assert  s.isOneBitCharacter([1,0,0]) is True, "WA"
    assert  s.isOneBitCharacter([1, 1, 1, 0]) is False, "WA"