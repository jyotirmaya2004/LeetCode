class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        mc=0
        for i in nums:
            if i==1:
                c+=1
                mc=max(c,mc)
            else:
                c=0
        return mc
                
        