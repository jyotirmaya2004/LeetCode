class Solution:
    def nextGreatestLetter(self, a: List[str], t: str) -> str:
        return a[bisect_right(a,t)%len(a)]