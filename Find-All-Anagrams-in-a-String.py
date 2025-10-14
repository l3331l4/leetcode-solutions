class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        
        have = {}
        have_total = 0
        need_total = len(need)
        res = []

        l = 0
        for r in range(len(s)):
            curr = s[r]
            if curr not in need:
                have.clear()
                have_total = 0
                l = r + 1
                continue

            have[curr] = have.get(curr, 0) + 1

            if have[curr] == need[curr]:
                have_total += 1

            while have[curr] > need.get(curr, 0):
                if s[l] in need and have[s[l]] == need[s[l]]:
                    have_total -= 1
                have[s[l]] -= 1
                l += 1

            if have_total == need_total and (r - l + 1) == len(p):
                res.append(l)
                if s[l] in have:
                    have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_total -= 1
                l += 1

        return res




