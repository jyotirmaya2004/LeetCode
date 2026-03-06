class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = len(s) - 1

        while i >= 0 and s[i] == '0':
            i -= 1

        while i >= 0:
            if s[i] == '0':
                return False
            i -= 1

        return True