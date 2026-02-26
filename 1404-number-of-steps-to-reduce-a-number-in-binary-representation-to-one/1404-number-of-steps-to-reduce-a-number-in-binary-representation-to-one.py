class Solution:
    def numSteps(self, s: str) -> int:
        return sum(reduce(lambda q,v:(q[0]+1+(v:=int(v)+q[1])%2,q[1]|v%2),s[:0:-1],(0,0)))