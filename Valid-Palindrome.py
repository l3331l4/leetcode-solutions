class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNum(c):
            if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z') or c in "0123456789"):
                return True
            return False

        newStr = ""
        for c in s:
            if isAlphaNum(c):
                newStr += c.lower()
        
        l = 0
        r = len(newStr) - 1

        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True
            