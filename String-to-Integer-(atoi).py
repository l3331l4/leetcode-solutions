class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        num = False
        sign = False
        start = 0

        s = s.lstrip()
        
        for i, c in enumerate(s):
            if c == "-":
                if sign or num:
                    return 0
                neg = True
                sign = True
                continue
            if c == "+":
                if sign or num:
                    return 0
                sign = True
                continue
            if c in "0123456789":
                num = True
                start = i
                end = i
                while end < len(s) and s[end] in "0123456789":
                    end += 1
                break
            else:
                return 0

        if not num:
            return 0

        print(start, end)

        INTMIN = - ( 2 ** 31)
        INTMAX = ( 2 ** 31) - 1


        
        if neg:
            if (0 - int(s[start:end])) < INTMIN:
                return INTMIN
            else:
                return 0 - int(s[start:end])
        else:
            if (int(s[start:end])) > INTMAX:
                return INTMAX
            else:
                return int(s[start:end])
