MOD = 10**9 + 7
facs = {}
facs[1] = 1
facs[2] = 2
for i in range(2,(10**5)+1):
    facs[i] = (facs[i-1] * i) % MOD

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        lowest = complexity[0]
        for c in complexity[1:]:
            if c <= lowest:
                return 0 
        return facs[len(complexity)-1]
        

