class Solution:
    def reverseVowels(self, s: str) -> str:
        st=[ch for ch in s if ch.lower() in "aeiou"]
        s1=list(s)
        j=1
        st1=list(st)
        for i in range(len(s1)):
            if s1[i].lower() in "aeiou":
                s1[i]=st1[-j]
                j+=1
        return "".join(s1)
        

        