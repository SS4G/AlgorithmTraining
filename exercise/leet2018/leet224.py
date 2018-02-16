class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        i = 0
        digitFlag = False
        tmpdigit = []
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif not digitFlag and self.isdigit(s[i]):
                tmpdigit = ""
                tmpdigit += s[i]
                digitFlag = True
                i += 1
            elif digitFlag and self.isdigit(s[i]):
                tmpdigit += s[i]
                i += 1
            elif digitFlag and not self.isdigit(s[i]):
                

            #if self.isdigit(s[i]):


    def isdigit(self, c):
        return c in "0123456789"
