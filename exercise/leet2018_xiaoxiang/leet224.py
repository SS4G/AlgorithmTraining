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
        s = "(" + s
        s = s + ")"
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue  # skip space
            elif not digitFlag and self.isdigit(s[i]):
                tmpdigit = ""
                tmpdigit += s[i]
                digitFlag = True
                i += 1
            elif digitFlag and self.isdigit(s[i]):
                tmpdigit += s[i]
                i += 1
            elif digitFlag and not self.isdigit(s[i]):
                arr.append(int(tmpdigit))
                digitFlag = False
            else:
                arr.append(s[i])
                i += 1
        #arr = ["(", ] + arr + [")", ]
        #print(arr)
        stack = []
        i = 0
        while i < len(arr):
            if arr[i] == ")":
                tmpArr = []
                while len(stack) > 0 and stack[-1] != '(':
                    tmpArr.append(stack.pop())
                stack.pop()  # pop (
                tmpArr.reverse()
                tmpRes = self.calcSingleExp(tmpArr)
                #print(tmpRes)
                stack.append(tmpRes)  # push new result to stack
            else:
                stack.append(arr[i])
            i += 1
        return stack[0]

    def calcSingleExp(self, expression):
        if not isinstance(expression[0], str):
            expression = ["+", ] + expression
        i = 0
        arr = []
        sign = '+'
        while i < len(expression):
            if i & 0x01 == 0:  # even sign
                sign = expression[i]
            else:  # odd number
                arr.append(expression[i] if sign == '+' else -expression[i])
            i += 1
        return sum(arr)

    def isdigit(self, c):
        return c in "0123456789"


if __name__ == "__main__":
    s = Solution()
    exp1 = "((1 +( 4+5 + 2)- 3) + ( 6 + 8 ) )"
    exp1 = "0"
    print(s.calculate(exp1))



    exp0 = ["-", 1, "+", 2, "-", 3]
    print(s.calcSingleExp(exp0))