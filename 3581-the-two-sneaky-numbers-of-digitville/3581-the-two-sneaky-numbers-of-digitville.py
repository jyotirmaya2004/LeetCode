class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]=2
            else:
                d[i]=1
        res=[]
        for i,k in d.items():
            if k==2:
                res.append(i)
        return res
        