class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNum(c):
            if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z') or c in "0123456789"):
                return True
            return False

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not (isAlphaNum(s[l])):
                l += 1

            while l < r and not (isAlphaNum(s[r])):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            