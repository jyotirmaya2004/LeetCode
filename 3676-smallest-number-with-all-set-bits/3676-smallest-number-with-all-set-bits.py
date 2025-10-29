class Solution:
    def smallestNumber(self, n: int) -> int:
        m=len(bin(n)[2:])
        s=0
        for i in range(m):
            s=s*10+1
        return int(str(s),2)