class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        sptr = 0
        gptr = 0
        cnt = 0
        while sptr < len(s) and gptr < len(g):
            if s[sptr] >= g[gptr]:
                cnt += 1
                sptr += 1
                gptr += 1
            else:
                sptr += 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    garr = [1,3,2]
    sarr = [1,2,1]
    print(s.findContentChildren(garr, sarr))
