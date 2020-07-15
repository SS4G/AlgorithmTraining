class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[None] * len(A) for i in range(len(B))]
        maxLength = 0 
        for i in range(len(A)):
            dp[i][0] = 1 if A[i] == B[0] else 0
            maxLength = max(maxLength, dp[i][0])
        for j in range(len(B)):
            dp[0][j] = 1 if A[0] == B[j] else 0
            maxLength = max(maxLength, dp[0][j])

        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLength = max(maxLength, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return maxLength