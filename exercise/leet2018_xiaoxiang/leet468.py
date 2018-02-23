class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if ":" in IP:
            res = self.validIPv6(IP)
            return "IPv6" if res else "Neither"
        elif "." in IP:
            res = self.validIPV4(IP)
            return "IPv4" if res else "Neither"
        else:    
            return "Neither"

    def validIPV4(self, IP):
        charSet = set(list("0123456789"))
        parts = IP.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if len(part) < 1:
                return False
            for c in part:
                if c not in charSet:
                    return False
            if not (0 <= int(part) <= 255):
                return False

            if part[0] == '0' and len(part) > 1:  # invalid leading zero
                return False
        return True

    def validIPv6(self, IP):
        charSet = set(list("0123456789abcdefABCDEF"))
        parts = IP.split(":")
        if len(parts) != 8:
            return False
        zeroFlag = False
        omtFlag = False
        for part in parts:
            if len(part) == 0:
                omtFlag = True

            if self.allZero(part):
                zeroFlag = True

            if len(part) > 4:
                return False

            for c in part:
                if c not in charSet:
                    return False
        if zeroFlag and omtFlag:
            return False
        return True

    def allZero(self, s):
        for i in range(len(s)):
            if s[i] != '0':
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    # print(s.validIPAddress("10.3.8.211"))
    print(s.validIPAddress("2001:0db8:85a3:0000::8a2e:0370:7334"))
    print(s.validIPAddress("2001:0db8:85a3:0000::8a2e:0370:7334"))