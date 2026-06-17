class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        ln = 0

        for c in s:
            if c == '*':
                ln = max(ln - 1, 0)
            elif c == '#':
                ln *= 2
            elif c != '%':
                ln += 1

        if k >= ln:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '*':
                ln += 1
            elif c == '#':
                if k >= ln // 2:
                    k -= ln // 2
                ln //= 2
            elif c == '%':
                k = ln - 1 - k
            else:
                if ln == k + 1:
                    return c
                ln -= 1