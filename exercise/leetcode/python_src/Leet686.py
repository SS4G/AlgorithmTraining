class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) > len(B):
            if B in A:
                return 1
            elif B in A * 2:
                return 2
            else:
                return -1
        else:
            if len(B) % len(A) == 0:
                if B in A * (len(B) // len(A)):
                    return len(B) // len(A)
                elif B in A * ((len(B) // len(A)) + 1):
                    return (len(B) // len(A)) + 1
            else:
                if B in A * ((len(B) // len(A)) + 1):
                    return len(B) // len(A)
                elif B in A * ((len(B) // len(A)) + 2):
                    return (len(B) // len(A)) + 2
            return -1