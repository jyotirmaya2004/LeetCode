class Solution:
    def myAtoi(self, s: str) -> int:
        r = ""
        t = 1
        i = 0
        n = len(s)
        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            t = -1 if s[i] == "-" else 1
            i += 1

        while i < n and s[i].isdigit():
            r += s[i]
            i += 1

        if r == "":
            return 0

        num = t * int(r)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

        

            
        