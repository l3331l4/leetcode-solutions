class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 1
        start = 0

        def expand(i, j):
            while (0 <= i < len(s)) and (0 <= j < len(s)) and (s[i] == s[j]):
                i -= 1
                j += 1
            return i+1, j-1
        
        for i in range(len(s)-1):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)
            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1
            if max(len1, len2) > maxLen:
                if len1 > len2:
                    maxLen = len1
                    start = l1
                else:
                    maxLen = len2
                    start = l2
            print(start, maxLen)

        return s[start:start+maxLen]

