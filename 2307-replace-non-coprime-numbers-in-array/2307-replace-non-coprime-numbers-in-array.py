import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:
            a=nums[i]
            b=nums[i+1]
            if math.gcd(a,b)>1:
                c=math.lcm(a,b)
                nums.pop(i)
                nums.pop(i)
                nums.insert(i,c)
                if i>0:
                    i-=1
            else:
                i+=1
        return nums

        