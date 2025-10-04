class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [ [False] * n for _ in range(n) ]
        # DP[i][j] = is char i to char j a palindrome
        start = 0
        end = 0
        maxLen = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):

                if s[i] == s[j]:
                    if (j == i + 1) or (dp[i+1][j-1]):
                        dp[i][j] = True
                        length = j - i + 1
                        if length > maxLen:
                            maxLen = length
                            start = i
                            end = j

        return s[start:end+1]
                        

        