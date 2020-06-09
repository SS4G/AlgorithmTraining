class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        str0 = str(num)
        translated = {}
        return self.translateNumDP(str0, translated)

    def translateNumDP(self, str0, translated):
        if len(str0) == 0:
            return 0
        elif len(str0) == 1:
            return 1
        elif len(str0) == 2:
            return 2 if int(str0) < 26 else 1
        elif str0 in translated:
            return translated[str0]
        elif 10 <= int(str0[:2]) < 26:
            translateNum = self.translateNumDP(str0[2:], translated) + self.translateNumDP(str0[1:], translated)
            translated[str0] = translateNum
            return translateNum
        else:
            translateNum = self.translateNumDP(str0[1:], translated)
            translated[str0] = translateNum
            return translateNum
