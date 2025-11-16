class Solution:
    def numSub(self, s: str) -> int:
        c=0
        n=0
        for i in s:
            if i=='0':
                c+=(n*(n+1))//2
                n=0
            else:
                n+=1
        c+=(n*(n+1))//2
        return c%((10**9)+7)
            