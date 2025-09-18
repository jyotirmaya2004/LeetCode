class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat=[num for r in grid for num in r]
        s=set(flat)
        r=sum(flat)-sum(s)
        n=len(s)+1
        m=(n*(n+1))//2-sum(s)
        return [r,m]
