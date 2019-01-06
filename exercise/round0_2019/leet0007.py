class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negFlag = False
        if x < 0:
            negFlag = True
        a = list(str(x))
        a.reverse()
        res = int("".join(map(str, a)))
        if negFlag:
            res = -res
        if res > 2**31-1 or res < -(2**31):
            return 0

if __name__ == "__main__":
    s = Solution()
    s.reverse(1)
    print(2**31)