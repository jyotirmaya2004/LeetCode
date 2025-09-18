class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum([ord(ch)for ch in t if t.isalpha()])-sum([ord(ch)for ch in s if s.isalpha()]))
        