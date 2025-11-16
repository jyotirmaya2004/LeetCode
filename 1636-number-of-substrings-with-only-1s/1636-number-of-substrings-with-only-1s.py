class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        count=0
        num=s.split('0')
        for n in num:
            m=len(n)
            if m>0:
                count+=(m*(m+1))//2
        return count%mod
