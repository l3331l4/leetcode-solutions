class Solution:
    def hasSameDigits(self, s: str) -> bool:
        st = s

        while len(st) > 2:
            st = []
            for i in range(len(s) - 1):
                num = (int(s[i]) + int(s[i+1])) % 10
                st.append(str(num))
            s = st

        return st[0] == st[1]
        
