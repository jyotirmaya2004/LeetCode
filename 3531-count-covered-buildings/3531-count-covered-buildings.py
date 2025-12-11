class Solution:
    def countCoveredBuildings(self, n: int, b: List[List[int]]) -> int:
        u,d,r,l = ([q]*-~n for q in [0,n,0,n])
        for x,y in b:
            u[x],d[x],l[y],r[y] = max(u[x],y),min(d[x],y),min(l[y],x),max(r[y],x)
        
        return sum(d[x]<y<u[x] and l[y]<x<r[y] for x,y in b)