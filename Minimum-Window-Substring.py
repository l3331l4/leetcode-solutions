class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        need = {}
        have = {}

        for c in t:
            need[c] = need.get(c, 0) + 1
        
        totalNeed = len(need)
        totalHave = 0

        l = 0
        r = 0
        currSubstring = ""

        while r < m:
            curr = s[r]
            if curr in need:
                have[curr] = have.get(curr, 0) + 1
                if have[curr] == need[curr]:
                    totalHave += 1
            
            while totalHave == totalNeed:
                currWindow = s[l:r+1]
                if (len(currSubstring) > len(currWindow)) or currSubstring == "":
                    currSubstring = currWindow

                if s[l] in need:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        totalHave -= 1
                l += 1        
            r += 1
    
        return currSubstring

            

            
        

        

