class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_v=0
        max_c=0
        for i in s:
            n=s.count(i)
            if i in "aeiou":
                if max_v<n:
                    max_v=n
            else:
                if max_c<n:
                    max_c=n
        return max_v+max_c

        