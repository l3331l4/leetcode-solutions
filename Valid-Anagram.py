class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_count = {}
        s_count = {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1

        for key in t_count:
            if key not in s_count:
                return False
            elif t_count[key] != s_count[key]:
                return False

        return True
