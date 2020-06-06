class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            if i == ' ':
                res.append("%20")
            else:
                res.append(i)
        return "".join(res)