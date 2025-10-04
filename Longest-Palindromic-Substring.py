class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 1
        starti = 0
        
        def expand(l, r):
            
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                l -= 1
                r += 1

            return l+1, r-1

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)
            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1
            
            if len1 >= len2:
                if len1 > maxLen:
                    maxLen = len1
                    starti = l1
            else:
                if len2 > maxLen:
                    maxLen = len2
                    starti = l2

        return s[starti:starti+maxLen] 


        